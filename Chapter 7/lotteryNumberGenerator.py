import random


def numberGenerator():
    numbers = [0] * 7
    index = 0

    while index < len(numbers):
        numbers[index] = random.randint(0, 9)
        index += 1

    return numbers


def displayNumbers(numbers):
    index = 0

    while index < len(numbers):
        print(numbers[index], end='')
        index += 1


lotteryNumbers = numberGenerator()
displayNumbers(lotteryNumbers)
