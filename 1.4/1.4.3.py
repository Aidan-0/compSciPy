import matplotlib.pyplot as plt
import os.path
import numpy as np
from PIL import Image

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))

# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')

# Read the image data into an array
# So plt wasn't working so I imported another thing and it seems to work
imgOrigin = Image.open(filename)
imgOrigin.load()
img = np.asarray( imgOrigin, dtype="int32" )

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot

# Make a rectangle of pixels yellow

ax[0].imshow(img, interpolation='none')
height = len(img)
width = len(img[0])
for r in range(155):
 for c in range(width):
    if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
        img[r][c]=[255,0,255] # red + green = yellow

ax[1].imshow(img, interpolation='none')

for r in range(420, 460):
 for c in range(130, 170):
    if sum(img[r][c])>400: # brightness R+G+B goes up to 3*255=765
        img[r][c]=[0,255,0] # red + green = yellow
ax[2].imshow(img, interpolation='none')

fig.show()