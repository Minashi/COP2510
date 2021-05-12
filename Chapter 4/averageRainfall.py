months = 12
monthsPassed = 0
totalInchesRainFall = 0

print("How many years?")
years = int(input())

for i in range(years):
    for x in range(months):
        monthsPassed += 1
        print("Month", monthsPassed, "\b: How many inches of rainfall?")
        amount = float(input())
        totalInchesRainFall += amount
else:
    averageRainFall = totalInchesRainFall/monthsPassed
    print("Number of months:", monthsPassed, "\nTotal Inches of Rainfall:", totalInchesRainFall,
          "\nAverage Rainfall per Month:", averageRainFall)
