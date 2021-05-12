insurance_Factor = 0.80


def insurance_Calculator(cost):
    insuranceCost = cost * insurance_Factor
    return insuranceCost


print("What is the replacement cost of the building?")
replacementCost = float(input())
print("Minimum amount of insurance to buy:", insurance_Calculator(replacementCost))
