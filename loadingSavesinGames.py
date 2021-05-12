def main():
    try:
        saveFile = open('save.txt', 'r')
        name = saveFile.readline()
        while name != '':
            age = saveFile.readline()
            breed = saveFile.readline()

            # name = name.rsplit('\n')
            # age = age.rsplit('\n')
            # breed = breed.rsplit('\n')

            print("Name:", name, end='')
            print("Age:", int(age))
            print("Breed:", breed)
            print("save loaded...")
            return
    except:
        saveFile = open('save.txt', 'w')
        saveFile.write("Tom\n")
        saveFile.write("6\n")
        saveFile.write("dog\n")
        print("New save created")
    finally:
        saveFile.close()


main()
