from time import sleep


def totalProfit():
    while True:
        print("Please enter amount of total sales")
        totalSales = float(input(">"))
        profit = totalSales * 0.23
        print("Your total profit from the total sales of $", totalSales, "is $", profit)
        sleep(1)
        print("Would you like to enter a new total of sales?")
        action = input(">")
        if action.lower() == 'no':
            return


totalProfit()
