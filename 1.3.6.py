import random


def roll2Dice():
    numbers = (1, 2, 3, 4, 5, 6)
    rand1 = random.choice(numbers)
    rand2 = random.choice(numbers)
    return (rand1 + rand2)

def guessLetter():
    # why
    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    secret = random.choice(alpha)
    user = input("What letter do you think it is? ")
    if secret == user:
        print ('Congratulations')
    else:
        print ('Wrong, the right one is', secret)