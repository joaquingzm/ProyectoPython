import cv2 as cv
import numpy as np
import copy
from pathlib import Path

#INICIO EJERCICIO 2

def levantar_imagen_grayscale(image_path):
    if not image_path.exists():
        image_path = input("\nHubo un error en el reconocimiento de la ruta de la imagen. Por favor ingrese la ruta completa de la imagen:\n")
    
    aux = cv.imread(str(image_path), cv.IMREAD_GRAYSCALE)
    return aux
    

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
    'Sharpening' : Sharpen
}


lista_keys = list(dic_kernels.keys())
"""Terminar input del usuario, la idea era que la persona elija de manera
ennumerada cual de los kernels quiere y en base a ese numero elegido acceder a la key en
esa posicion y con esa key acceder a la matriz. El print de las opciones se puede hacer
con un for in dic_kernels.key() o algo así"""

print('Elegir filtro a aplicar:')
for i,k in enumerate(dic_kernels.keys(),start=1):
    print(i,' - ',k,'\n')
key_kernel = lista_keys[int(input())-1]

image_path = Path('/ProyectoPython/Imagenes/Computadora_grises.jpg')

d = levantar_imagen_grayscale(image_path) 

mascara_booleana = np.zeros(d.shape, dtype=bool)



kernel = dic_kernels[key_kernel]

coef = kernel.shape[0]//2

d_copy = copy.deepcopy(d)   #esto genera una copia completa de la matriz, copia a la cual le aplicaremos el kernel

y = d_copy[coef:-coef,coef:-coef]   #Esto hace que la variable y sea la submatriz que no incluye los bordes de la matriz original, segun corresponda para cada kernel

mascara_booleana[:coef,:] = True
mascara_booleana[-1:-coef-1:-1,:] = True
mascara_booleana[:,:coef] = True
mascara_booleana[:,-1:-coef-1:-1] = True

bordes = int(input("\nIndique mediante el respectivo numero que desea hacer con los bordes en la imagen con el filtro:\n1-Poner los bordes en negro, 2-Poner los bordes en blanco, 3-Mantener los bordes\n"))

#De esta forma se puede hacer el kernel e ignorar los bordes
for indice,valor in (np.ndenumerate(y)):
    y[indice]= np.sum(d[indice[0]:indice[0] + kernel.shape[0], indice[1]:indice[1] + kernel.shape[0]]*kernel)
      
if bordes==1 or bordes==2:
    valores = [0,255]
    d_copy[mascara_booleana]=valores[bordes-1]

cv.imshow("ImgAlterada",d_copy)
cv.imshow('ImgOriginal',d)
cv.waitKey(0)

cv.destroyAllWindows()


#FIN EJERCICIO 2