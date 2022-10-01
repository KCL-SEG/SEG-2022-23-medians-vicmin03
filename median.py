"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if (len(numbers)&2 == 0):
            no1 = numbers[(len(numbers)/2)-1]
            no2 = numbers[len(numbers)/2]
            print((no1+no2)/2)
        else:
            print(numbers[len(numbers)])

    except ValueError:
        checkIndex = int(len(numbers)/2)
        print(numbers[checkIndex])
    else:
        break

