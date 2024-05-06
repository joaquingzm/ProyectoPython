import cv2
import numpy as np

img = cv2.imread("OpenCV/Images/Computadora.jpg")
a,b,c = cv2.split(img) 
#Me da las matrices de cada canal
imgGris = np.zeros(a.shape,dtype=np.uint8)



print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            aux = np.sum(img[i][j])/3
            '''Si sumo cada elemento por separado el dato que devuelve es de 8 bits, en cambio 
            si utilizo np.sum() el método devuelve un dato que pueda contener la suma
            '''
            if aux>255: imgGris[i][j]=255
            else: imgGris[i][j]=aux


print(img[1][1])
cv2.imshow('Imagen Gris',imgGris)
cv2.imshow('Imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows