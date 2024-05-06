import cv2 as cv
import numpy as np


#INICIO EJERCICIO 1
img =  cv.imread('OpenCV/Images/Computadora.jpg')
img2 = cv.imread('OpenCV/Images/Computadora.jpg',0)
a,b,c = cv.split(img)
print(a,b,c)

d = np.zeros((a.shape), np.uint16)
d += a
d += b
d += c
d //= 3
d *=256

cv.imshow("imgGris", d)
cv.imshow("imaGris2",img2)

cv.waitKey(0)

cv.destroyAllWindows()

#FIN EJERCICIO 1
'''
#INICIO EJERCICIO 2

x = np.array([
    [1,2,3,90],
    [4,5,6,90],
    [7,8,9,90],
    [1,2,3,90]
])

y = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#Forma A de ignorar los bordes con el kernel
mask = np.ones(x.shape, dtype=bool)

mask[:,0] = False
mask[:,-1] = False
mask[0,:] = False
mask[-1,:] = False

x[mask] +=2

print(x)


#De esta forma se puede hacer el kernel e ignorar los bordes
for indice,valor in (np.ndenumerate(x)):
    if ((indice[0] != 0) and (indice[1] != 0) and (indice[0] != x.shape[0]-1) and (indice[1] != x.shape[1]-1)):
        x[indice] += 2
        
print(x)

#FIN EJERCICIO 2
'''