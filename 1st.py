import random

total = 100
num_values = 9
min_range = 14
max_range = 15

# Calculate the maximum and minimum possible values based on the total and number of values
max_value = total - (num_values - 1) * min_range
min_value = total - (num_values - 1) * max_range

# Choose random values within the range and adjust for the total value
values = [random.uniform(min_value, max_value)]
for i in range(num_values - 1):
    remaining_total = total - sum(values)
    remaining_num_values = num_values - (i + 1)
    max_value = remaining_total - (remaining_num_values - 1) * min_range
    min_value = remaining_total - (remaining_num_values - 1) * max_range
    value = random.uniform(min_value, max_value)
    values.append(value)

# Display the values
print(values)