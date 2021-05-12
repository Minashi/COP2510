numberOfDays = 0
totalCollected = 0

while numberOfDays < 7:
    numberOfDays += 1
    print("Day", numberOfDays, '\b:', "How many bugs have you collected?")
    collected = int(input(">"))
    totalCollected = totalCollected + collected
else:
    print("You have collected", totalCollected, "bugs in", numberOfDays, "days.")

