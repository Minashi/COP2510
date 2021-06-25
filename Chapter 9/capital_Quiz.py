import random

dictionary = {'Alabama': 'Montgomery',
              'Alaska': 'Juneau',
              'Arizona': 'Phoenix',
              'Arkansas': 'Little Rock',
              'California': 'Sacramento',
              'Colorado': 'Denver',
              'Connecticut': 'Hartford',
              'Delaware': 'Dover',
              'Florida': 'Tallahassee',
              'Georgia': 'Atlanta',
              'Hawaii': 'Honolulu',
              'Idaho': 'Boise',
              'Illinois': 'Springfield',
              'Indiana': 'Indianapolis',
              'Iowa': 'Des Moines',
              'Kansas': 'Topeka',
              'Kentucky': 'Frankfort',
              'Louisiana': 'Baton Rouge',
              'Maine': 'Augusta',
              'Maryland': 'Annapolis',
              'Massachusetts': 'Boston',
              'Michigan': 'Lansing',
              'Minnesota': 'Saint Paul',
              'Mississippi': 'Jackson',
              'Missouri': 'Jefferson City',
              'Montana': 'Helena',
              'Nebraska': 'Lincoln',
              'Nevada': 'Carson City',
              'New Hampshire': 'Concord',
              'New Jersey': 'Trenton',
              'New Mexico': 'Santa Fe',
              'New York': 'Albany',
              'North Carolina': 'Raleigh',
              'North Dakota': 'Bismarck',
              'Ohio': 'Columbus',
              'Oklahoma': 'Oklahoma City',
              'Oregon': 'Salem',
              'Pennsylvania': 'Harrisburg',
              'Rhode Island': 'Providence',
              'South Carolina': 'Columbia',
              'South Dakota': 'Pierre',
              'Tennessee': 'Nashville',
              'Texas': 'Austin',
              'Utah': 'Salt Lake City',
              'Vermont': 'Montpelier',
              'Virginia': 'Richmond',
              'Washington': 'Olympia',
              'West Virginia': 'Charleston',
              'Wisconsin': 'Madison',
              'Wyoming': 'Cheyenne'}


correct_Counter = 0
false_Counter = 0


def should_Run(correct_Counter, false_Counter):
    while correct_Counter != 50:
        return
    else:
        print("Score:")
        print(correct_Counter, " correct")
        print(false_Counter, " false")
        exit()


def quiz():
    global correct_Counter
    global false_Counter
    global dictionary
    state, capital = random.choice(list(dictionary.items()))

    print("What is the capital for", state, '?')
    guess = input('>')
    if guess.lower() == 'exit':
        print("Score:")
        print(correct_Counter, " correct")
        print(false_Counter, " false")
        exit()
    elif guess.lower() == capital.lower():
        print("Correct! +1 points\n")
        del dictionary[state]
        correct_Counter += 1
        return correct_Counter, false_Counter
    else:
        print("Incorrect!\n")
        false_Counter += 1
        return correct_Counter, false_Counter


print("This is a quiz for the US states and capitals!")


while True:
    c, f = quiz()
    should_Run(c, f)
