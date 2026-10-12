# Worksheet 1.2: Task Solution
from util import read_numbers
import sys

try :
    numbers = read_numbers()

    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / len(numbers)

    numbers.sort()
    middle = len(numbers)// 2

    if len(numbers) % 2 == 1:
        median = numbers[middle]

    else:
        median = (numbers[middle-1] + numbers[middle]) / 2

    print(f"Minimum = {minimum}")
    print(f"Maximun = {maximum}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")

except ValueError:
    if len(numbers) == 0:
        sys.exit("Error: no numbers provided") 
