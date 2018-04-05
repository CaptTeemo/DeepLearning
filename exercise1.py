# Exercise 1.
# Generate ten images with different gray levels of foreground and background and label images.
import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.colors import NoNorm

def createImage(foreground):
    im_image =100*np.ones((28,28), dtype=np.uint8)
    im_image[1:3, 1:3] = foreground
    return im_image

if __name__ == '__main__':

    liImages = []

    x = 255
    for i in range(0,10):
        liImages.append(createImage(x))
        x = x - 20
        plt.imshow(liImages[0] , cmap=pylab.gray() , norm=NoNorm())

   # plt.imshow(liImages[4] , cmap=pylab.gray() , norm=NoNorm())
    plt.show()
    