@startuml
start
: Load an image;
: Covert image to double and devide by 255 to normalise;
: display image;
: Computer image gradient (imgradientxy(sobel));
: show gradient image and (gx+4)/8 to shift values due to sobel;
: obtain the magnitude and direction/n;
: show the magnitude grad;
: show the grad direction;
@enduml

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('Macclaren.png', 0)