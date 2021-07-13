class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_Number, pay_Rate):
        super().__init__(name, number)
        self.__shift_Number = shift_Number
        self.__pay_Rate = pay_Rate

    def set_shift_number(self, shift_Number):
        self.__shift_Number = shift_Number

    def set_pay_rate(self, pay_Rate):
        self.__pay_Rate = pay_Rate

    def get_Shift_Number(self):
        return self.__shift_Number

    def get_Pay_Rate(self):
        return self.__pay_Rate


employee = ProductionWorker(None, None, None, None)
repeat = True
counter = 1


def input_Info():
    print("Please enter the information for the employee:")
    name = input('Name: ')
    number = input('Employee Number: ')
    shift_Number = input("(Day = 1, Night = 2) Shift Number: ")
    pay_Rate = input('Pay Rate: ')

    employee.set_name(name)
    employee.set_number(number)
    employee.set_shift_number(shift_Number)
    employee.set_pay_rate(pay_Rate)


def display_Info():
    print("Name: ", employee.get_name())
    print("Employee Number: ", employee.get_number())
    print("Shift Number: ", employee.get_Shift_Number())
    print("Pay Rate: ", employee.get_Pay_Rate())


input_Info()
display_Info()
