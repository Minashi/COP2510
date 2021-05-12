file = open('names.txt', 'r')
line = file.readline()

x = 0

while line != '':
    x += 1
    line = file.readline()

file.close()
print(x)

