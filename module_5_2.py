import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, float, float]:
    for number in re.finditer(r'\b\d+.\d+\b', text):
        yield float(number.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, float, float]]) -> float:
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_profit = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_profit}")