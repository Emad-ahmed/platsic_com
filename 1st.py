import random
total = 160.00
range_min = 14.00
range_max = 15.00

numbers = []

while total >= range_max:
    num = random.uniform(range_min, range_max)
    num = round(num, 2)
    numbers.append(num)
    total -= num

numbers.append(total)  # Add the remaining value to the list


print(sum(numbers))
print("Numbers:", numbers)