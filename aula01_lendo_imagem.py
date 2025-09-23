import cv2

# Função imread

img = cv2.imread('assets/fotos/nical.jpg.jpeg')
img_1 = cv2.imread('assets/fotos/cat_large.jpg')
img_2 = cv2.imread('assets/fotos/cats 2.jpg')

# Função imshow[]
cv2.imshow('Janela do gato', img)
cv2.imshow('janelão do gato',img_1)
cv2.imshow('gatinho',img_2)

# função waitKey[] 'K' Maisculo
cv2.waitKey(0)