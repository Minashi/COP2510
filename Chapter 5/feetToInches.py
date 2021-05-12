foot = 12


def feet_to_inches(feet):
    inches = feet * 12
    return inches


print("Enter a number of feet:")
feet = float(input())
print(feet_to_inches(feet))
