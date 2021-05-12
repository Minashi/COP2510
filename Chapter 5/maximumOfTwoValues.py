def maximum(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 'The integers are both equal'


print("Please enter two integer values:")
values = input()
x, y = [int(n) for n in values.split()]

print(maximum(x, y))
