import cv2 as cv
import numpy as np
from pathlib import Path


#INICIO EJERCICIO 1

#FALTA:
#GENERALIZAR LA ENTRADA DE LA IMAGEN

nombre_imagen = input("Ingrese el nombre de una imagen junto al formato: ")

image_path = str(Path(f'/ProyectoPython/Imagenes/{nombre_imagen}'))

img =  cv.imread(image_path)
b,g,r = cv.split(img)


d_uint8= r//3 + g//3 + b//3   #Grayscale con promedio pesado

h=r*0.3 + g*0.59 + b*0.11

d_uint8 = d_uint8.astype(np.uint8)

print(d_uint8)

print(d_uint8)

cv.imshow("imgColor",img)
cv.imshow("imgGris", d_uint8)
cv.imwrite("Computadora_grises.jpg",d_uint8)

cv.waitKey(0)

cv.destroyAllWindows()

#FIN EJERCICIO 1

