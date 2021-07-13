class Pet:
    def __init__(self, name, animalType, age):
        self.__name = name
        self.__animal_type = animalType
        self.__age = age

    def set_name(self, newName):
        self.__name = newName

    def set_animal_type(self, newAnimalType):
        self.__animal_type = newAnimalType

    def set_age(self, newAge):
        self.__age = newAge

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


print("What is the name of your pet?")
name = input('>')
print("What kind of pet is it?")
animal_Type = input('>')
print("How old is your pet?")
age = input('>')

pet_1 = Pet(name, animal_Type, age)




print(pet_1.get_name())










# def main():
#     print("Hello, what is your pets name?")
#     name = input('>')
#     print("What kind of pet is it?")
#     animalType = input('>')
#     print("How old is ", )
#     age = input('>')
#     global pet1
#     pet1 = Pet(name, animalType, age)
#     pet1.set_name(name)
#     pet1.set_animal_type(animalType)
#     pet1.set_age(age)
#
#
# def return_attributes():
#     print("Stats:")
#     print("Name: ", pet1.get_name())
#     print("Type: ", pet1.get_type())
#     print("Age: ", pet1.get_age())
#
#
# main()
# return_attributes()

