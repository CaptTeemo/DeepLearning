# Imports
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.colors import NoNorm
import pylab
from scipy import misc
import numpy as np


im_image =100*np.ones((28,28), dtype=np.uint8)   # Image (Größe, DatenTyp) Wert der Pixel = 100*1
im_image[1:3, 1:3] = 200                       # Bearbeiten von Pixel-Werten

plt.subplot(121) # Plotten in Ausgabe: Reihe, Spalte, Index

#plt.gray()
plt.imshow(im_image , cmap='gray', norm=NoNorm())
#plt.imshow(im_image , cmap=pylab.gray() , norm=NoNorm())  #Colormaps aus anderen Paketen
#plt.imshow(im_image , cmap=plt.cm.gray, norm=NoNorm())
#plt.show()

plt.imsave('pout.jpg', im_image) # (Pillow integriert) Bild speichern


im_label=im_image<120  #Neues Bild mit Werten < 120 herausgefiltert
im_label=np.zeros((28,28), dtype=bool)
im_label[1:3, 1:3] =np.array([[True, True] , [True, True]]) # Einzelne Pixel im 2D-Array an und ausschalten
plt.subplot(122)

# Eigentliche Ausgabe der Plots
plt.imshow(im_label , cmap=plt.cm.binary)
plt.show()
plt.imsave('pout.jpg', im_label) # uses the Image module (PIL)


# Store data to disk, and load it again:
#>>> np.save('/tmp/123', np.array([[1, 2, 3], [4, 5, 6]]))
#>>> np.load('/tmp/123.npy')
#array([[1, 2, 3],
#       [4, 5, 6]])

#arr = np.array(img) transform image to array
#arr = img.load() load array
#a=np.ones(10, dtype=bool)
#https://matplotlib.org/users/image_tutorial.html
#https://stackoverflow.com/questions/3823752/display-image-as-grayscale-using-matplotlib/11603881
