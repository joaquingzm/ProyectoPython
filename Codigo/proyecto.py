import cv2 as cv
import numpy as np


#INICIO EJERCICIO 1

#FALTA:
#GENERALIZAR LA ENTRADA DE LA IMAGEN

img =  cv.imread('D:\\ProyectoPython\\Imagenes\\Computadora.jpg')
b,g,r = cv.split(img)


d=r*0.3 + g*0.59 + b*0.11   #Grayscale con promedio pesado

d_normalized = np.clip(d,0,255)  #Esta linea es para asegurar que los valores de la matriz estan entre 0-255 porque sino se van a generar errores en el imshow
d_uint8 = d_normalized.astype(np.uint8)

print(d_uint8)

cv.imshow("imgColor",img)
cv.imshow("imgGris", d_uint8)
cv.imwrite("Computadora_grises.jpg",d_uint8)

cv.waitKey(0)

cv.destroyAllWindows()

#FIN EJERCICIO 1

