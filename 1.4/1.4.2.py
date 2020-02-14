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
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')

ax[1].set_xlim(7, 17)
ax[1].set_ylim(35, 45)
ax[1].imshow(img, interpolation='none')

ax[2].set_xlim(17, 27)
ax[2].set_ylim(45, 55)
ax[2].imshow(img, interpolation='none')

# Show the figure on the screen
fig.show()
