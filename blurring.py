import cv2
import numpy as np

img = cv2.imread('my.jpg')
cv2.imshow('orignal', img)

cv2.waitKey(0)
matrix = np.ones((3, 3), np.float32)/9
blurr = cv2.filter2D(img, -1, matrix)
cv2.imshow('blur', blurr)

cv2.waitKey(0)
matrix2 = np.ones((9, 9), np.float32)/81
blurr2 = cv2.filter2D(img, -1, matrix2)
cv2.imshow('blur2', blurr2)

cv2.waitKey(0)
cv2.destroyAllWindows()