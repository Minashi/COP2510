def areaOfRectangle(length, width):
    area = length * width
    return area


print("What is the length of the first rectangle?")
length_1 = float(input())
print("What is the width of the first rectangle?")
width_1 = float(input())
print("What is the length of the second rectangle?")
length_2 = float(input())
print("What is the width of the second rectangle?")
width_2 = float(input())

area_1 = areaOfRectangle(length_1, width_1)
area_2 = areaOfRectangle(length_2, width_2)

if area_1 == area_2:
    print("Both rectangles have the same area of", area_1)
elif area_1 > area_2:
    print("The first rectangle has a larger area by", area_1 - area_2)
else:
    print("The second rectangle has a larger area by", area_2 - area_1)
