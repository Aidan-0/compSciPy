'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
'''Read the image data'''
# Get the directory of this python script

directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot

ax[0].imshow(img, interpolation='none')

ax[1].plot(43, 35, 'ro')
ax[1].plot(68, 30, 'ro')
ax[1].imshow(img, interpolation='none')

ax[2].set_xlim(7, 17)
ax[2].set_ylim(45, 35)
ax[2].imshow(img, interpolation='none')

ax[3].set_xlim(17, 27)
ax[3].set_ylim(45, 35)
ax[3].imshow(img, interpolation='none')

ax[4].set_xlim(27, 37)
ax[4].set_ylim(45, 35)
ax[4].imshow(img, interpolation='none')

# Show the figure on the screen
fig.show()
