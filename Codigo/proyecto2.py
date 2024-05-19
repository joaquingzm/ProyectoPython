import cv2 as cv
import numpy as np
import copy

#INICIO EJERCICIO 2

#FALTA:
#GENERALIZAR LA ENTRADA DEL KERNEL

#Ya realizado:
#GENERALIZAR LA CREACION DE y (creo que se haria multiplicando a cada numero del slicing por kernel.shape[0]//2)

#Inicio de cambios
Desenfoque_Gaussiano = (1 / 256.0)*np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
])
Desenfoque_Normalizado = (1/9)*np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])
Deteccion_Vertical = np.array([
    [0.25,0,-0.25],
    [0.5,0,-0.5],
    [0.25,0,-0.25]
])
Deteccion_Horizontal = np.array([
    [0.25,0.5,0.25],
    [0,0,0],
    [-0.25,-0.5,-0.25]    
])
Sharpen = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
dic_kernels = {
    'Desenfoque Gaussiano' : Desenfoque_Gaussiano,
    'Desenfoque Normalizado' : Desenfoque_Normalizado,
    'Deteccion Ejes Verticales' : Deteccion_Vertical,
    'Deteccion Ejes Horizontales' : Deteccion_Horizontal,
    'Sharpen' : Sharpen
}
lista_keys = list(dic_kernels.keys())
"""Terminar input del usuario, la idea era que la persona elija de manera
ennumerada cual de los kernels quiere y en base a ese numero elegido acceder a la key en
esa posicion y con esa key acceder a la matriz. El print de las opciones se puede hacer
con un for in dic_kernels.key() o algo así"""

d = cv.imread('/home/joaquin/Universidad/Python/ProyectoPython/Imagenes/Computadora_grises.jpg',cv.IMREAD_GRAYSCALE)  #Es necesario el segundo parametro para que la imagen no se cargue con 3 canales (daria error)
#Fin de cambios
x = np.array([
    [1,2,3,90],
    [4,5,6,90],
    [7,8,9,90],
    [1,2,3,90]
])


kernel = dic_kernels['Deteccion Ejes Horizontales']#Modifiqué

coef = kernel.shape[0]//2

d_copy = copy.deepcopy(d)   #esto genera una copia completa de la matriz a la cual le aplicaremos el kernel
y = d_copy[1*coef:-1*coef,1*coef:-1*coef]   #esto hace que Y apunte solo al sector de d sin los bordes (hay que modificarlo para hacerlo generico)


#De esta forma se puede hacer el kernel e ignorar los bordes
for indice,valor in (np.ndenumerate(y)):
    y[indice]= np.sum(d[indice[0]:indice[0] + kernel.shape[0], indice[1]:indice[1] + kernel.shape[0]]*kernel)
      
print(d_copy)
cv.imshow("ImgAlterada",d_copy)
cv.imshow('ImgOriginal',d)#Modifiqué
cv.waitKey(0)

cv.destroyAllWindows()


#FIN EJERCICIO 2