import json
import os
import logging

log_filename = os.path.join(os.getcwd(), 'json__Lytvynenko.log')
logging.basicConfig(filename=log_filename, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

directory = os.path.join(os.getcwd(), 'work_with_json')


def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        if 'Expecting' in e.msg:
            hint = "→ Відсутня кома або дужка"
        else:
            hint = "→ Помилка синтаксису JSON"
        return False, f"{e.msg} (рядок {e.lineno}, стовпець {e.colno}). {hint}"


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if filename.endswith('.json'):
        is_valid, error_message = validate_json(file_path)
        if not is_valid:
            logging.error(f"Файл {filename} невалідний JSON. Помилка: {error_message}")

print(f"Результат логування записан у файл {log_filename}")
