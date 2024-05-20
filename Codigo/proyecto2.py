import cv2 as cv
import numpy as np
import copy
from pathlib import Path

#INICIO EJERCICIO 2

def levantar_imagen_grayscale(image_path):
    if not image_path.exists():
        image_path = input("\nHubo un error en el reconocimiento de la ruta de la imagen. Por favor ingrese la ruta completa de la imagen:\n->")
    
    """La lectura de la imagen en escala de grises la realizamos con el parametro cv.IMREAD_GRAYSCALE para 
    que dicha imagen se lea con un solo canal porque, a pesar de guardarla en el anterior punto en escala de grises,
    la carga de esa imagen se realiza con 3 canales si utilizamos cv.imread() sin el parametro que aclare que se cargue
    la imagen como un unico canal"""
    
    aux = cv.imread(str(image_path), cv.IMREAD_GRAYSCALE)
    return aux
    
#Creacion de los filtros a elegir por parte del usuario
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

#Creacion del diccionario de elementos 
dic_kernels = {
    'Desenfoque Gaussiano' : Desenfoque_Gaussiano,
    'Desenfoque Normalizado' : Desenfoque_Normalizado,
    'Deteccion Ejes Verticales' : Deteccion_Vertical,
    'Deteccion Ejes Horizontales' : Deteccion_Horizontal,
    'Sharpening' : Sharpen
}


#Creacion de una lista con los nombres de los filtros a partir de las claves ('keys') del diccionario
lista_keys = list(dic_kernels.keys())

#Entrada de la ruta de la imagen y control
img_predeterminada = int(input('\nSeleccione opciones:\n1 - Procesar imagen predeterminada\n2 - Procesar imagen que se encuentre dentro de la carpeta Imagenes\n->'))
if img_predeterminada==2:
    eleccion_img =  input('Ingrese nombre de una imagen, que se encuentre dentro de la carpeta Imagenes, junto con su formato:\n->')
else:
    eleccion_img = 'Foto.jpg'
    
image_path = Path(f'/ProyectoPython/Imagenes/{eleccion_img}')
img_gris = levantar_imagen_grayscale(image_path) 

#Seleccion del filtro a aplicar
print('\nElegir filtro a aplicar:')
for i,k in enumerate(dic_kernels.keys(),start=1):
    print(i,' - ',k)
key_kernel = lista_keys[int(input("\nIngrese el numero correspondiente al filtro elegido:\n->"))-1]

#Asignacion del filtro a la variable kernel
kernel = dic_kernels[key_kernel]

#Creacion de la variable coef para determinar el tamaño del borde a acotar de la imagen ingresada para realizar correctamente la convolución
coef = kernel.shape[0]//2

#Generación de una copia completa de la matriz, copia a la cual le aplicaremos la convolución
img_gris_alterada = copy.deepcopy(img_gris)   

#Creacion de la variable sub_img como un puntero a la parte de la matriz a la que aplicaremos el kernel (no incluye los bordes para que no haya problemas durante la convolución)
sub_img = img_gris_alterada[coef:-coef,coef:-coef]   

"""Creacion de una mascara booleana, que se utilizará para hacer indexación booleana sobre la matriz
a la que se aplicará la convolución para obtener los bordes NO utilizados durante la convolución.
Implica tener una serie de valores True (verdadero) y False (falso) que corresponden a las filas o columnas 
que queremos seleccionar o no de una estructura de datos, respectivamente."""
mascara_booleana = np.zeros(img_gris.shape, dtype=bool)
mascara_booleana[:coef,:] = True
mascara_booleana[-1:-coef-1:-1,:] = True
mascara_booleana[:,:coef] = True
mascara_booleana[:,-1:-coef-1:-1] = True

#Creación de la variable bordes para determinar qué hacer con los bordes de la imagen a la que se aplicó un filtro
bordes = int(input("\nIndique mediante el respectivo numero que desea hacer con los bordes en la imagen con el filtro:\n1-Poner los bordes en negro\n2-Poner los bordes en blanco\n3-Mantener los bordes\n->"))

#Realizacion de la convolucion, a partir de sub_img
"""Dentro de un bucle FOR se recorre sub_img mientras se va asignando en cada una de sus posiciones la suma de
todos elementos de la matriz resultante de haber utilizado la operacion de multiplicacion entre dos matrices definida
en la libreria Numpy (esta multiplicacion se realiza posicion a posicion, como si fuera una suma matricial tradicional).
Las matrices que se multiplican son la matriz que indica el kernel y la matriz formada por el elemento en sub_img en la 
posicion indice (indice se modifica en cada iteración) y los elementos que este tenga alrededor.
Los condicionales estan truncar los valores que pueda dar la operacion de convolución en caso de que sean mayores que 255
o menores que 0."""

for indice,valor in (np.ndenumerate(sub_img)):
    resultado = np.sum(img_gris[indice[0]:indice[0] + kernel.shape[0], indice[1]:indice[1] + kernel.shape[0]]*kernel)
    if resultado>255:
        resultado = 255
    elif resultado<0:
        resultado = 0
    sub_img[indice]= resultado


#Se realiza una cambio en los bordes, si así se eligió      
if bordes==1 or bordes==2:
    valores = [0,255]
    img_gris_alterada[mascara_booleana]=valores[bordes-1]


eleccion_img = eleccion_img.replace('.', 'Gris_alterada.') 
cv.imshow("ImgAlterada",img_gris_alterada)
cv.imshow('ImgOriginal',img_gris)
cv.imwrite(f"Imagenes/{eleccion_img}",img_gris_alterada)
cv.waitKey(0)

cv.destroyAllWindows()


#FIN EJERCICIO 2