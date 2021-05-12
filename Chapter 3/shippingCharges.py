print("          Weight of Package                Rate per Pound")
print("Over 2 pounds but not more than 6 pounds--------$3.00")
print("Over 6 pounds but not more than 10 pounds-------$4.00")
print("Over 10 pounds----------------------------------$4.75")


def shippingCharge(weight):
    if weight <= 2:
        charge = 1.50
        return charge
    elif 2 < weight <= 6:
        charge = 3.00
        return charge
    elif 6 < weight <= 10:
        charge = 4.00
        return charge
    elif weight > 10:
        charge = 4.75
        return charge


while True:
    print("\nPlease enter the weight of the package:")
    weight_1 = float(input(">"))
    charge = shippingCharge(weight_1)
    print("The charge for a package that weighs", weight_1, "is", charge)
    print("\nWould you like to do another package?")
    action = input(">")
    if action == 'no':
        break
