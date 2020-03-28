import cv2
import numpy as np

img = cv2.imread('my.jpg')
cv2.imshow('Orignal', img)
cv2.waitKey(0)

matrix = np.zeros(img.shape, np.uint8)+50

add = cv2.add(img, matrix)
cv2.imshow('Add', add)

sub = cv2.subtract(img, matrix)
cv2.imshow('Sub', sub)

mul = cv2.multiply(img, matrix)
cv2.imshow('Mul', mul)




cv2.waitKey(0)
cv2.destroyAllWindows()