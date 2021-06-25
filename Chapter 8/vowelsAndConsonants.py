vowels = ['a', 'e', 'i', 'o', 'u']


def checkVowels(string):
    vowel_counter = 0
    for letter in string:
        if letter in vowels:
            vowel_counter += 1

    return vowel_counter


def checkConsonants(string):
    consonant_counter = 0
    for letter in string:
        if letter not in vowels:
            consonant_counter += 1

    return consonant_counter


string = input('Please input a string of letters: ').lower()
print('There are', checkVowels(string), 'vowels')
print('There are', checkConsonants(string), 'consonants')

