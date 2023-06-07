import random

def split_number(target_sum, min_value, max_value):
    if target_sum < min_value or target_sum > max_value:
        return None

    remaining_sum = target_sum
    numbers = []

    while remaining_sum > 0:
        number = random.randint(min_value, max_value)
        number = min(number, remaining_sum)
        numbers.append(number)
        remaining_sum -= number

    return numbers

target_sum = 180
min_value = 8
max_value = 14

result = split_number(target_sum, min_value, max_value)

if result:
    print("Split numbers:", result)
    print("Sum:", sum(result))
else:
    print("No valid split exists.")