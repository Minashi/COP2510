numbersFile = open('numbers.txt', 'r')

line = numbersFile.readline()

while line != '':
    print(line, end='')
    line = numbersFile.readline()

numbersFile.close()
