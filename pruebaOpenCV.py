import cv2
import numpy as np


img = cv2.imread('OpenCV/Images/NaveEspacial.png',1)
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('OpenCV/Images/new_image.png',img)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows