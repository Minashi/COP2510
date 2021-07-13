class Person:
    def __init__(self, name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone_number


class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number, trueorfalse):
        super().__init__(name, address, telephone_number)
        self.__customer_number = customer_number
        self.__mailing_list = False


counter = 1
repeat = True
customer_list = []


while repeat:
    print("Please enter the following information of the customer: ")
    name = input('Name: ')
    address = input('Address: ')
    telephone_Number = input("Telephone Number: ")
    mailing_list = input("Does the customer want to be on the mailing list? True/False\n")

    customer = Customer(name, address, telephone_Number, counter, mailing_list)
    customer_list.append(customer)
    counter += 1

    answer = input("Do you want to enter another customers information?")
    if answer.lower() == 'no':
        repeat = False

