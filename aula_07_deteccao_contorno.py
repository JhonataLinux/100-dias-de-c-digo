import cv2
import numpy as np

img = cv2.imread('assets/fotos/cats.jpg')
#cv2.imshow('foto',img)  

#desenha um canva branco do mesmo tamanho que a imagem de trabalho
black = np.zeros(img.shape, dtype='uint8')
#cv2.imshow('black', black)

#Transferiado para cinzar
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#2. Detecção de contornos


#a. Borrar a imagem com GaussianBlue

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('blur', blur)

#B. função de canny
canny = cv2.Canny(blur, 125,175)
cv2.imshow('canny', canny)

# Novidade dessa aula
#cv2.findContourns(imagem,modo_detecção, metodo_aproximação_contorno)
#recomendo -> cv3.RETR-LIST, recomendado pelo propria documentação
#Metodos de aproximação
#cv2.CHAIN_APPROX_NONE: salva absolutamente todos os pontos de contorno, custoso, imagina se tivesse apenas uma linha
#cv2.CHAIN_APPROX_SIMPLE: ele remove todos os pontos redundantes e comprime o contorno, economizando memoria

contorno, hier = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contorno)} contornos encontrado')
cv2.drawContours(black, contorno, -1, (0,0,255), 1)
cv2.imshow('contorno',black)

cv2.waitKey()