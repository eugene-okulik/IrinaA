import os
import argparse


def search_logs(log_folder, search_text):
    results = []
    for root, dirs, files in os.walk(log_folder):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for line_number, line in enumerate(lines, start=1):
                    if search_text in line:
                        results.append({
                            'file': file_path,
                            'line_number': line_number,
                            'text': line.strip()
                        })
    return results


def print_results(results):
    if results:
        print("Результаты поиска:")
        for result in results:
            print(f"Файл: {result['file']}, Строка: {result['line_number']}, Текст: {result['text']}")
    else:
        print("Логи не содержат указанный текст.")


if __name__ == "__main__":
    # Получение пути к файлу
    script_path = os.path.abspath(__file__)

    # Получение директории, в которой находится файл
    script_dir = os.path.dirname(script_path)

    parser = argparse.ArgumentParser(description="Logs Analyzer")
    parser.add_argument("log_folder", type=str, help="Путь к папке с логами")
    parser.add_argument("--text", type=str, help="Текст для поиска")
    args = parser.parse_args()

    log_folder = args.log_folder
    search_text = args.text

    if not os.path.exists(log_folder):
        print("Указанный путь не существует.")
    else:
        results = search_logs(log_folder, search_text)
        print_results(results)
