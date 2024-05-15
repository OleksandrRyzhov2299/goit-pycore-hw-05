import re


def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    matches = re.finditer(pattern, text)
    for match in matches :
         yield float(match.group())

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."         
for numbers in generator_numbers(text): 
     print(numbers)        


def sum_profit(text: str, func: generator_numbers):
    total_profit = sum(generator_numbers(text))
    return total_profit



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total}")
