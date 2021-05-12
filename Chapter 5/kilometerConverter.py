def converter_Kilo_To_Miles(kilometers):
    miles = kilometers * 0.6214
    return miles


print("Please enter a distance in kilometers:")
distance_Kilometer = float(input())

print(converter_Kilo_To_Miles(distance_Kilometer))
