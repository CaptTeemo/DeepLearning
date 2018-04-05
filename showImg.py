
import matplotlib.pyplot as plt
from scipy import ndimage
import matplotlib.image as mpimg
from matplotlib.colors import NoNorm
import pylab
from scipy import misc
import numpy as np

# Display image
img=mpimg.imread('pout.jpg')   # read image png format
plt.imshow(img)
plt.show()
