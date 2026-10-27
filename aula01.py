import cv2

imagem = cv2.imread("coca cola espumante.jpg")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem em tons de cinza', cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()