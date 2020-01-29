import random


def rando():
   print(random.randint(1, 4))


def go_guess():
   '''A simple guessing game'''
   
   # Initialize variables
   # Number is in between so we don't include 1 or 20
   low = 1
   high = 100
   number = random.randint(low + 1, high - 1)
   tries = 0
   guess = 0

   print('I have a number between', low, 'and', high)
   while (guess != number):
      guess = int(input('Guess: '))
      if guess > number:
         print('Too high, guess again')
         tries += 1
      else:
         print('Too low, guess again')
         tries += 1
   print('Congrats! My number was', number,
         '! You guessed in', tries, 'tries!')


def validate():
    guess='1'  # initialization with a bad guess
    answer='hangman word'
    while guess not in answer:
        guess=input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
