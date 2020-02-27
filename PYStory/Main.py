import random as rndm
from Tkinter import *
from PIL import Image, ImageTk
from os import path

def cover():
    print('bruh')

def story():
    print('Starting.')

# print('Choose your own adventure: [Concept Name]')
# print('By Aidan-0')

# userChoice = (raw_input('Type "go" to continue, type anything else to cancel: ')).upper()
# if userChoice == 'GO':
#     story()
# else:
#     print('Ending program...')

root = Tk()
canvas = Canvas(root, height=750, width=750, relief=RAISED, bg='#e0e0e0')
canvas.grid()

cube1 = canvas.create_polygon(
    150, 150, 
    150, 400, 
    400, 500, 
    400, 250, fill='#f5f5f5'
)
cube2 = canvas.create_polygon(
    400, 500,
    400, 250,
    600, 150,
    600, 375, fill='gray'
)
cube3 = canvas.create_polygon(
    150, 150,
    400, 250,
    600, 150,
    380, 50, fill='#5e5e5e'
)


img = ImageTk.PhotoImage(Image.open('a.jpg'))
imaging = canvas.create_image(200, 500, image=img)
root.mainloop()