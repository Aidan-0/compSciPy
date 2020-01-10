# from __future__ import print_function # must be first in file
import random


def quiz_decimal(low, high):
    print ('Type a number between', low, 'and', high)
    userinput = float(input('Number: '))
    if userinput > high:
        print ('Nope,', userinput, 'is greater than', high)
    elif userinput < low:
        print ('Nope,', userinput, 'is less than', low)
    elif low < userinput < high:
        print ('Correct!', low, '<', userinput, '<', high)
    else:
        return ('fatal error, please try again')


def guess_once():
 secret = random.randint(1, 4)
 print 'I have a number between 1 and 4.'
 guess = int(raw_input('Guess: '))
 if guess != secret:
    if guess > secret:
        print 'Too high - my number was', secret
    else:
        print 'Too low - my number was', secret
 else:
    print 'Right, my number is', guess


def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'


def function(n):
     if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                return n, "is a multiple of 6"
            else:
                return n, "is even"
        else:
            return n, "is odd"
    else:
        return n, "is not an integer"


