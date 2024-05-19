import cv2 as cv
import numpy as np
import copy

#INICIO EJERCICIO 2

#FALTA:
#GENERALIZAR LA ENTRADA DEL KERNEL

#Ya realizado:
#GENERALIZAR LA CREACION DE y (creo que se haria multiplicando a cada numero del slicing por kernel.shape[0]//2)

d = cv.imread('D:\\ProyectoPython\\Imagenes\\Computadora_grises.jpg',cv.IMREAD_GRAYSCALE)  #Es necesario el segundo parametro para que la imagen no se cargue con 3 canales (daria error)

x = np.array([
    [1,2,3,90],
    [4,5,6,90],
    [7,8,9,90],
    [1,2,3,90]
])


kernel = (1 / 256.0) * np.array([[1, 4, 6, 4, 1],
                                   [4, 16, 24, 16, 4],
                                   [6, 24, 36, 24, 6],
                                   [4, 16, 24, 16, 4],
                                   [1, 4, 6, 4, 1]])

coef = kernel.shape[0]//2

d_copy = copy.deepcopy(d)   #esto genera una copia completa de la matriz a la cual le aplicaremos el kernel
y = d_copy[1*coef:-1*coef,1*coef:-1*coef]   #esto hace que Y apunte solo al sector de d sin los bordes (hay que modificarlo para hacerlo generico)


#De esta forma se puede hacer el kernel e ignorar los bordes
for indice,valor in (np.ndenumerate(y)):
    y[indice]= np.sum(d[indice[0]:indice[0] + kernel.shape[0], indice[1]:indice[1] + kernel.shape[0]]*kernel)
      
print(d_copy)
cv.imshow("ImgAlterada",d_copy)

cv.waitKey(0)

cv.destroyAllWindows()


#FIN EJERCICIO 2