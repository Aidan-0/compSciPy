from PIL import Image
import os.path

# remove the next 2 lines if you already have qt5 configured
# if not, please type
# %mathplotlib qt5
# in ipy or it will not display anything
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

# for *slightly* faster processing
# ok it's more than twice as fast
from threading import Thread

# TL - Top left
# TR - Top right
# BL - Bottom left
# BR - Bottom right
def brightColorsTopLeft():
    for r in range(0, int(height/2)):
        for c in range(0, int(width/2)):
            if sum(img[r][c])>brightSpots: 
                img[r][c]=[0,0,255]
    print ('Bright areas colored (TL)')

def brightColorsTopRight():
    for r in range(0, int(height/2)):
        for c in range(int(width/2), width):
            if sum(img[r][c])>brightSpots: 
                img[r][c]=[0,0,255]
    print ('Bright areas colored (TR)')  

def brightColorsBotLeft():
    for r in range(int(height/2), height):
        for c in range(0, int(width/2)):
            if sum(img[r][c])>brightSpots: 
                img[r][c]=[0,0,255]
    print ('Bright areas colored (BL)')

def brightColorsBotRight():
    for r in range(int(height/2), height):
        for c in range(int(width/2), width):
            if sum(img[r][c])>brightSpots: 
                img[r][c]=[0,0,255]
    print ('Bright areas colored (BR)') 

def darkColorsTopLeft():
    for r in range(0, int(height/2)):
        for c in range(0, int(width/2)):
            if sum(img[r][c])<darkSpots: 
                img[r][c]=[0,255,0]
    print ('Dark areas colored (TL)')

def darkColorsTopRight():
    for r in range(0, int(height/2)):
        for c in range(int(width/2), width):
            if sum(img[r][c])<darkSpots: 
                img[r][c]=[0,255,0]
    print ('Dark areas colored (TR)')

def darkColorsBotLeft():
    for r in range(int(height/2), height):
        for c in range(0, int(width/2)):
            if sum(img[r][c])<darkSpots: 
                img[r][c]=[0,255,0]
    print ('Dark areas colored (BL)')

def darkColorsBotRight():
    for r in range(int(height/2), height):
        for c in range(int(width/2), width):
            if sum(img[r][c])<darkSpots: 
                img[r][c]=[0,255,0]
    print ('Dark areas colored (BR)')

def borderTopLeft():
    for r in range(0, int(height/2)):
        for c in range(0, int(width/2)):
            if r not in range(border, height - border) or c not in range(border, width - border):
                img[r][c] = [255, 0, 0]
    print ('Border Colored (TL)')

def borderTopRight():
    for r in range(0, int(height/2)):
        for c in range(int(width/2), width):
            if r not in range(border, height - border) or c not in range(border, width - border):
                img[r][c] = [255, 0, 0]
    print ('Border Colored (TR)')

def borderBottomLeft():
    for r in range(int(height/2), height):
        for c in range(0, int(width/2)):
            if r not in range(border, height - border) or c not in range(border, width - border):
                img[r][c] = [255, 0, 0]
    print ('Border Colored (BL)')

def borderBottomRight():
    for r in range(int(height/2), height):
        for c in range(int(width/2), width):
            if r not in range(border, height - border) or c not in range(border, width - border):
                img[r][c] = [255, 0, 0]
    print ('Border Colored (BR)')

# region reading img

# getting file path
dirname = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dirname, 'faceForSummativeWha.jpg')

# reading with PIL.Image
imgOrigin = Image.open(file)
imgOrigin.load()

# assign the image to a numpy array
img = np.asarray(imgOrigin, dtype="int32" )

# endregion

fig, ax = plt.subplots(1, 2)

ax[0].imshow(img, interpolation='none')

# variables for the functions defined in lines (14 - 91)
darkSpots = 200
brightSpots = 500
border = 100
height = len(img)
width = len(img[0])

# region Multi-threading
# defining all threads to methods
t1 = Thread(target=brightColorsTopLeft, name='t1')
t2 = Thread(target=brightColorsTopRight, name='t2')
t3 = Thread(target=brightColorsBotLeft, name='t3')
t4 = Thread(target=brightColorsBotRight, name='t4')
t5 = Thread(target=darkColorsTopLeft, name='t5')
t6 = Thread(target=darkColorsTopRight, name='t6')
t7 = Thread(target=darkColorsBotLeft, name='t7')
t8 = Thread(target=darkColorsBotRight, name='t8')
t9 = Thread(target=borderTopLeft, name='t9')
t10 = Thread(target=borderTopRight, name='t10')
t11 = Thread(target=borderBottomLeft, name='t11')
t12 = Thread(target=borderBottomRight, name='t12')

# start bright and dark coloring
t1.start() 
t2.start() 
t3.start()
t4.start()
t5.start() 
t6.start() 
t7.start()
t8.start()

# wait until all bright threads are finished
t1.join() 
t2.join() 
t3.join()
t4.join()
# endregion

# starting after so it doesn't fill the border and others
t9.start()
t10.start()
t11.start()
t12.start()

# drawing the red circles
ax[1].plot(983, 1590, 'ro')
ax[1].plot(1400, 1550, 'ro')

# left ear yellow box
for r in range(1631, 1914):
    for c in range(632, 725):
        img[r][c] = [255, 255, 0]
print('Left ear drawn')

# right ear yellow box
for r in range(1600, 1880):
    for c in range(1760, 1844):
        img[r][c] = [255, 255, 0]
print('Right ear drawn')

# waits until all other threads finish
t5.join() 
t6.join() 
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()

# write that processed image to ax
ax[1].imshow(img, interpolation='none')

# spice it up a little
plt.title("Hello :)")