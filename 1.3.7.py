import random
import matplotlib.pyplot as plt

plt.ion()  # sets “interactive on”: figures redrawn when updated


def dice(n):
    sumDice = 0
    for number in range(n):
        sumDice += random.randint(1, 6)
    print('Roll was', sumDice)


def matches(ticket, winner):
    matching = 0
    for number in ticket:
        if number in winner:
            matching += 1
    print(matching)


def rollonehundred():
    a = []
    for number in range(0, 100):
        a += [random.randint(1, 6)]
    plt.hist(a)
    plt.show()

def hangman(guessed, secret):
    reveal = ''
    for char in secret:
        if char in guessed:
            reveal += char
        else:
            if char == ' ':
                reveal += ' '
            else:
                reveal += '-'
    print (reveal)

def picks():
    a = []  # make an empty list

    # Why all the brackets below?
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()


def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS':
        print(day + 'day')
    for day in range(5, 8):
        print('It is the ' + str(day) + 'th of September')
