import sys
from pathlib import Path
from pprint import pprint
from collections import Counter

"""
Реалізуйте функцію 
parse_log_line(line: str) -> dict 
для парсингу рядків логу.
"""
def parse_log_line(line: str) -> dict:
    """
    Розділяємо строку на частини: час, рівень логування та повідомлення
    Використовуємо maxsplit, щоб обмежити кількість розділів до чотирьох
    """
    parts = line.strip().split(maxsplit=3)  
    """
    Створюємо словник з відповідними ключами та значеннями
    """
    log_dict = {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "message": parts[3]
    }
    
    return log_dict

"""
Реалізуйте функцію 
load_logs(file_path: str) -> list 
для завантаження логів з файлу.
"""
def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as file:
        # Створюємо список та заповнюємо його словниками
        lines = [parse_log_line(line) for line in file.readlines()]
    return lines
    
"""
Реалізуйте функцію
filter_logs_by_level(logs: list, level: str) -> list 
для фільтрації логів за рівнем.
"""
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]

"""
Реалізуйте функцію
count_logs_by_level(logs: list) -> dict 
для підрахунку записів за рівнем логування.
"""
def count_logs_by_level(logs: list) -> dict:
    return dict(Counter([log['level'] for log in logs]))
    
"""
Результати мають бути представлені у вигляді таблиці з 
кількістю записів для кожного рівня. 
Для цього реалізуйте функцію 
display_log_counts(counts: dict), яка форматує та виводить результати. 
Вона приймає результати виконання функції count_logs_by_level.
"""
def display_log_counts(counts: dict):
    print('Рівень логування | Кількість\n-----------------|----------')
    for key, value in counts.items():
        print(f'{key}\t\t | {value}')

if __name__ == "__main__":
    if not Path(sys.argv[1]).exists():
        print(f'Файл "{sys.argv[1]}" не існує.')
    else:
        if len(sys.argv) == 2:
            display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))
        elif len(sys.argv) == 3:
            display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))
            print(f"\nДеталі логів для рівня '{sys.argv[2].lower()}':")
            logs_by_level = filter_logs_by_level(load_logs(sys.argv[1]), sys.argv[2])
            for item in logs_by_level:
                print(f'{item['timestamp']} - {item['message']}')