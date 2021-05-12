from time import sleep


def milesPerGallon():
    while True:
        print("How many miles have you traveled?")
        milesTraveled = float(input())
        print("How many gallons of gas did you use?")
        gasUsed = float(input())
        mpg = milesTraveled/gasUsed
        print("Miles per Gallon:", mpg)
        sleep(1)
        print("Do you want to find MPG again?")
        action = input()
        if action == 'no':
            return


milesPerGallon()
