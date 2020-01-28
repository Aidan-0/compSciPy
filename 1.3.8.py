import random


def rando():
   print(random.randint(1, 4))


def go_guess():
   '''THIS CODE WILL AT THIS POINT CAUSE A LOOP THAT CAN ONLY BE BROKEN BY INTERRUPT
   PLEASE ONLY PROCEED IF YOU HAVE THIS'''
   
   # Number is in between so we don't include 1 or 20
   randint = random.randint(2, 19)
   gusses = 0
   print('I have a number between 1 and 20')
   guess = int(input('Guess: '))
   while int(input('Guess: ') != randint:
      if int(input('Guess: ') > randint:
         print('Too high, guess again')
         gusses += 1
      else:
         print('Too low, guess again')
         gueses += 1
   print('Congrats! My number was', randint,
         '! You guessed in', gueses, 'tries!')


def validate():
    guess='1'  # initialization with a bad guess
    answer='hangman word'
    while guess not in answer:
        guess=input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
