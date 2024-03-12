import os
import argparse
from datetime import datetime
from colorama import Fore, Style


# Функция для обработки блока лога
def process_log_block(file_path, block, results, search_text, start_date, end_date, unwanted_text):
    timestamp_str = block[0].split()[0]  # Извлекаем временную метку из первой строки блока
    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        # Пропускаем блок, если не удалось распознать временную метку
        return

    # Проверяем соответствие времени блока заданным критериям
    if start_date and timestamp < start_date:
        return
    if end_date and timestamp > end_date:
        return

    # Объединяем строки блока в одну для поиска текста целиком
    block_text = ''.join(block)

    # Поиск текста в блоке
    if search_text and search_text not in block_text:
        return

    # Фильтрация блока по нежелательному тексту
    if unwanted_text and unwanted_text in block_text:
        return

    # Если блок прошел все проверки, добавляем его в результаты
    results.append({
        'file': file_path,
        'line_number': block[0].split()[1][:-1],  # Извлекаем номер строки из первой строки блока
        'text': block_text.strip()
    })


# Функция для поиска логов в указанной директории
def search_logs(log_folder, search_text, start_date, end_date, unwanted_text):
    results = []
    for root, dirs, files in os.walk(log_folder):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                current_block = []  # Хранит текущий блок лога
                for line in lines:
                    current_block.append(line)
                    if line.startswith("["):
                        # Нашли начало нового блока, обрабатываем предыдущий
                        process_log_block(file_path, current_block, results, search_text, start_date, end_date,
                                          unwanted_text)
                        current_block = [line]  # Начинаем новый блок с текущей строкой

                # Обрабатываем последний блок после выхода из цикла
                process_log_block(file_path, current_block, results, search_text, start_date, end_date, unwanted_text)

    return results


# Функция для вывода результатов поиска
def print_results(results, full_output=False):
    if results:
        print("Результаты поиска:")
        for result in results:
            start_index = max(result['text'].find(search_text) - 150, 0)  # Начало вывода 150 симв до найденного текста
            end_index = min(result['text'].find(search_text) + 150, len(result['text']))  # Конец вывода 150 симв после
            highlighted_text = (
                result['text'][:start_index]
                + Fore.RED
                + result['text']
            [start_index:end_index]
                + Style.RESET_ALL  # Выделение найденного текста красным
                + result['text'][end_index:]
            )
            print(f"Файл: {Fore.BLUE}{result['file']}{Style.RESET_ALL}, Строка: {Fore.GREEN}{result['line_number']}"
                  f"{Style.RESET_ALL}, Текст: {highlighted_text}")
            if full_output:
                print(result['text'])
            print()
    else:
        print("Логи не содержат указанный текст.")


if __name__ == "__main__":
    # Получение пути к файлу
    script_path = os.path.abspath(__file__)

    # Получение директории, в которой находится файл
    script_dir = os.path.dirname(script_path)

    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Logs Analyzer 2")
    parser.add_argument("log_folder", type=str, help="Путь к папке с логами")
    parser.add_argument("--text", type=str, help="Текст для поиска")
    parser.add_argument("--start_date", type=str, help="Дата начала поиска в формате 'YYYY-MM-DD HH:MM:SS.SSS'")
    parser.add_argument("--end_date", type=str, help="Дата окончания поиска в формате 'YYYY-MM-DD HH:MM:SS.SSS'")
    parser.add_argument("--unwanted_text", type=str, help="Текст, который нужно исключить из результатов поиска")
    parser.add_argument("--full_output", action="store_true", help="Вывести полный текст найденных блоков логов")
    args = parser.parse_args()

    log_folder = args.log_folder
    search_text = args.text
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d %H:%M:%S.%f") if args.start_date else None
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d %H:%M:%S.%f") if args.end_date else None
    unwanted_text = args.unwanted_text
    full_output = args.full_output

    if not os.path.exists(log_folder):
        print("Указанный путь не существует.")
    else:
        results = search_logs(log_folder, search_text, start_date, end_date, unwanted_text)
        print_results(results, full_output)
