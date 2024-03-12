import os
import argparse
from datetime import datetime
from colorama import Fore, Style


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
        print(f"Текст '{search_text}' не найден в блоке:")
        print(block_text)
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


def search_logs(log_folder, search_text, start_date, end_date, unwanted_text):
    results = []
    print(f"Ищем текст: '{search_text}'")
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


def print_results(results, full_output=False):
    if results:
        print("Результаты поиска:")
        for result in results:
            text = result['text']
            # Находим индекс начала искомого текста
            start_index = text.find(search_text)
            # Выводим 150 символов перед искомым текстом
            start_highlight = max(0, start_index - 150)
            # Выводим 150 символов после искомого текста
            end_highlight = min(len(text), start_index + len(search_text) + 150)
            # Выделение цветом
            highlighted_text = (
                text[start_highlight:start_index]
                + Fore.RED
                + text[start_index:start_index + len(search_text)]
                + Style.RESET_ALL
                + text[start_index + len(search_text):end_highlight]
            )
            # Выводим результат с выделением цветом
            print(f"Файл: {result['file']}, Строка: {result['line_number']}, Текст: {highlighted_text}")
            if full_output:
                print(text)
            print()
    else:
        print("Логи не содержат указанный текст.")


if __name__ == "__main__":
    # Получение пути к файлу
    script_path = os.path.abspath(__file__)

    # Получение директории, в которой находится файл
    script_dir = os.path.dirname(script_path)

    parser = argparse.ArgumentParser(description="Logs Analyzer 2")
    parser.add_argument("log_folder", type=str, help="Путь к папке с логами")
    parser.add_argument("--text", type=str, default=None, help="Текст для поиска")
    parser.add_argument("--start_date", type=str, default=None, help="Дата начала поиска в формате 'YYYY-MM-DD HH:MM:SS.SSS'")
    parser.add_argument("--end_date", type=str, default=None, help="Дата окончания поиска в формате 'YYYY-MM-DD HH:MM:SS.SSS'")
    parser.add_argument("--unwanted_text", type=str, default=None, help="Текст, который надо исключить из результатов поиска")
    parser.add_argument("--full_output", action="store_true", help="Вывести полный текст найденных блоков логов")
    args = parser.parse_args()

    log_folder = args.log_folder
    search_text = args.text  # Присвоение значения аргумента --text
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d %H:%M:%S.%f") if args.start_date else None
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d %H:%M:%S.%f") if args.end_date else None
    unwanted_text = args.unwanted_text
    full_output = args.full_output

    if not os.path.exists(log_folder):
        print("Указанный путь не существует.")
    else:
        results = search_logs(log_folder, search_text, start_date, end_date, unwanted_text)
        print_results(results, full_output)
