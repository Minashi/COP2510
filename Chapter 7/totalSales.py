def storeSales():
    week = 7
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    dayCounter = 0
    index = 0
    sales = [0] * 7

    while dayCounter < week and index < len(sales):
        dayCounter += 1
        print("Sales for day", days[index], "\b:")
        sales[index] = int(input())
        index += 1
    return sales


def displayTotalSales(sales):
    index = 0
    totalSales = 0

    while index < len(sales):
        totalSales += sales[index]
        index += 1

    totalSales = str(totalSales)
    print("Total Sales for the week:", '$' + totalSales)


weekSales = storeSales()
displayTotalSales(weekSales)
