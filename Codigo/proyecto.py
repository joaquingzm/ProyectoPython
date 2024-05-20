import cv2 as cv
import numpy as np
from pathlib import Path

#INICIO EJERCICIO 1

def levantar_imagen(img_path):
    if not img_path.exists():
        img_path = input('Hubo un error con el path a la imagen, por favor copiar y pegar la ruta completa de la imagen:\n->')
    aux = cv.imread(str(img_path))
    b,g,r = cv.split(aux)
    return aux,b,g,r


#Inicializacion de variables

prom_p = np.array([[1/3,1/3,1/3],[0.3,0.59,0.11]], dtype=np.float32)
img_predeterminada = int(input('Seleccione opciones:\n1 - Procesar imagen predeterminada\n2 - Procesar imagen que se encuentre dentro de la carpeta Imagenes\n->'))
if img_predeterminada==2:
    eleccion_img =  input('Ingrese nombre de una imagen, que se encuentre dentro de la carpeta Imagenes, junto con su formato:\n->')
else:
    eleccion_img = 'Foto.jpg'


#Levantando la imagen

"""La utilizacion de la libreria pathlib y, especificamente, del modulo Path es para dar robustez a la ruta de 
la imagen debido a que la ruta de archivos no se determina de igual manera en todos los sistemas operativos.
Path entonces se especializa en establecer la ruta de un archivo segun le corresponde al sistema operativo de la
computadora en donde se este ejecutando el programa (por ejemplo Windows o Linux)."""

image_path = (Path(f'/ProyectoPython/Imagenes/{eleccion_img}'))
img,b,g,r = levantar_imagen(image_path)
elec_g = int(input('Seleccione el tipo de conversion a escala de grises segun el respectivo numero:\n1-Promedio, 2-Promedio pesado\n->'))

#Procesando imagen, operación generalizada para distintas escalas de grises
"""El calculo se realiza con las operaciones entre matrices ya integradas en la libreria
numpy debido a que se encuentran optimizadas. El algoritmo de multiplicación por un escalar es
de orden O(n) debido a que la matriz se guarda en posiciones de memoria contiguas, teniendo
así que recorrer un "arreglo de una dimension" para realizar el cálculo."""

img_gris= r*prom_p[elec_g-1,0] + g*prom_p[elec_g-1,1] + b*prom_p[elec_g-1,2]  
img_gris = img_gris.astype(np.uint8)


#Mostrando imagen

eleccion_img = eleccion_img.replace('.', 'Gris.') 
cv.imshow("imgColor",img)
cv.imshow("imgGris", img_gris)
cv.imwrite(f"Imagenes/{eleccion_img}",img_gris)
cv.waitKey(0)
cv.destroyAllWindows()


#FIN EJERCICIO 1

