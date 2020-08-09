# -*- coding: utf-8 -*-
"""
Read Image
@idMoteb
"""


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



# Load an color image in grayscale
img = cv.imread('people.jpg',0)



plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


"""# Load an color image in color
img = cv.imread('sherman.jpg',1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()



# Load an color image in color
img = cv.imread('sherman.jpg',1)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

