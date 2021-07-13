class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def __str__(self):
        return "\nDescription: " + self.__description + "\nUnits in Inventory: " + self.__units + "\nPrice: " + \
               self.__price


counter = 0
items_List = []
descriptions = ['Jacket', 'Designer Jeans', 'Shirt']
units_In_Inventory = ['12', '40', '20']
prices = ['59.95', '34.95', '24.95']


def main():
    global counter
    while counter < 3:
        set_attributes(descriptions[counter], units_In_Inventory[counter], prices[counter])
        counter += 1
    get_attributes()


def set_attributes(description, unit, price):
    global items_List
    item = RetailItem(description, unit, price)
    items_List.append(item)


def get_attributes():
    for item in items_List:
        print(item)


main()
