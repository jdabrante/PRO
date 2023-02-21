import sys

values = sys.argv[1:]

int_values = [int(number) for number in values]
avg = sum(int_values) / len(int_values)

print(avg)
