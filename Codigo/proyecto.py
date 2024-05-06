import cv2 as cv
import numpy as np
import copy


#INICIO EJERCICIO 1

#FALTA:
#GENERALIZAR LA ENTRADA DE LA IMAGEN

img =  cv.imread('D:\\ProyectoPython\\Imagenes\\nada evangelizar ven a mi.jpg')
img2 = cv.imread('D:\\ProyectoPython\\Imagenes\\nada evangelizar ven a mi.jpg',0)
a,b,c = cv.split(img)


d = np.zeros((a.shape), np.uint16)
d += a
d += b
d += c
d //= 3
d *=256

cv.imshow("imgColor",img)
cv.imshow("imgGris", d)
cv.imshow("imaGris2",img2)

print(d)

#FIN EJERCICIO 1

#INICIO EJERCICIO 2

#FALTA:
#GENERALIZAR LA ENTRADA DEL KERNEL
#GENERALIZAR LA CREACION DE y (creo que se haria multiplicando a cada numero del slicing por kernel.shape[0]//2)

x = np.array([
    [1,2,3,90],
    [4,5,6,90],
    [7,8,9,90],
    [1,2,3,90]
])


kernel = np.array([
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]
])


d_copy = copy.deepcopy(d)   #esto genera una copia completa de la matriz a la cual le aplicaremos el kernel
y = d_copy[1:-1,1:-1]   #esto hace que Y apunte solo al sector de d sin los bordes (hay que modificarlo para hacerlo generico)


#De esta forma se puede hacer el kernel e ignorar los bordes
for indice,valor in (np.ndenumerate(y)):
    y[indice]= np.sum(d[indice[0]:indice[0] + kernel.shape[0], indice[1]:indice[1] + kernel.shape[0]]*kernel)
      
print(d_copy)
cv.imshow("ImgAlterada",d_copy)

cv.waitKey(0)

cv.destroyAllWindows()


#FIN EJERCICIO 2
