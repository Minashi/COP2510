def input_name():
    print("Please enter your first, middle, and last name.")
    full_name = input().lower().split()
    return full_name


def output(full_name):
    first_name = full_name[0]
    FI = first_name[0]
    middle_name = full_name[1]
    MI = middle_name[0]
    last_name = full_name[2]
    LI = last_name[0]

    print(FI.upper(), '\b.', MI.upper(), '\b.', LI.upper(), '\b.')


name = input_name()
output(name)

