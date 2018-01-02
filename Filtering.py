import numpy as np
import cv2
import matplotlib
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from scipy import ndimage
import scipy.misc

@startuml
start
: Use an image as a filter;
 if(work hard) then (yes)
    :process all;
else(no)
:process yes;
endif


@enduml

def scale(imgs, factor):
    result = imgs.dot(factor)
    return result

# Load an color image in grayscale
img = cv2.imread('Macclaren.png', 0)  # load image as colour image Arg 0 = greyscale, 1 = RGB
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# Create a gaussian filter

bsize = 81  #define the size of the gaussiasn filter matrix
sigma = 5  # deifne the sigma, i.e how wide is the width

#img = cv2.GaussianBlur(img, (bsize, bsize), sigma)# use opencv to apply a gaussian filter
filter = cv2.getGaussianKernel(bsize,sigma) #create the guassian filter kernal


# fig = plt.figure()  # create a plotting  instance
# ax = fig.gca(projection='3d')  # plot in 3D for vieiwng
#
# # Make Data
# X = np.arange(-10, 10, float(20 / hsize))  # Create the X axis data, must be same length as gaussian size
# Y = np.arange(-10, 10, float(20 / hsize))  # Create the Y axis data, must be same length as gaussian size
# X, Y = np.meshgrid(X, Y)  # port X, Y to mesh grid...
#
# # Create the plotting surface
# surf = ax.plot_surface(X, Y, filter, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
# # set plot limits and format
# ax.set_zlim(np.amin(filter), np.amax(filter))
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# fig.colorbar(surf, shrink=0.5, aspect=5)  # size colour bar for resolution

#Convolve filter and image and take care of the corners
#img = ndimage.convolve(img, filter, mode='reflect') #Correlate can be replace to convolve instead
noisy = img + 0.1 * img.std() * np.random.random(img.shape)

#plt.show()
cv2.imshow("Image", noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()
