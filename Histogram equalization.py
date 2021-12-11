# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:30:09 2021

@author: smita.kiran
"""

import os
os.getcwd()
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
Image = cv2.imread(r"C:/Users/smita.kiran/Desktop/SK/Pic.jpg",0)
cv2.imshow('image',Image)
cv2.waitKey(0)
cv2.destroyAllWindows()
np.shape(Image)
Image.show
# Image1=cv2.equalizeHist(Image)
hist,bins = np.histogram(Image.flatten(),256,[0,256])
#cummulative sum of elememts along the given axis
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(Image.flatten(),256,[0,256], color = 'r')
# The xlim() function in pyplot module of matplotlib library is used to get or set the x-limits of the current axes
plt.xlim([0,256])
# The attribute Loc in legend() is used to specify the location of the legend.
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
