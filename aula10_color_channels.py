import cv2  
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')


blank = np.zeros(img.shape[:2], dtype='uint8')
#Desintegrado imagem
b, g , r = cv2.split(img)
#cv2.imshow('BLue', b)
#cv2.imshow('Grean',g)   
#cv2.imshow('Red', r)
#Reintregando img canais de cor 
blue =cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

#cv2.imshow('cor', blue)
#cv2.imshow('co', green)
#cv2.imshow('c',red)

# Reintegrando a imagem
marged = cv2.merge([b, g, r])
cv2.imshow('med',marged)
print(marged.shape)
print(img.shape)


cv2.waitKey(0)
