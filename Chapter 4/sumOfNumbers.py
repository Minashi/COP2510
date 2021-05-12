total = 0

print("Please enter a series of positive numbers.\nEnter a negative number to calculate the sum.")
number = float(input())

while number >= 0:
    total += number
    number = float(input())
else:
    print("The total sum of the positive series of numbers is", total)
