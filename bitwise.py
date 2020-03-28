import cv2
import numpy as np

square = np.zeros((300, 300), dtype="uint8")

cv2.rectangle(square, (30, 30), (250, 250), 255, -1)
cv2.imshow('square', square)

cv2.waitKey(0)
ellipse = np.zeros((300, 300), dtype="uint8")
cv2.ellipse(ellipse, (150, 150), (150, 150), 0, 300, 0, 255, -1)
cv2.imshow('ellipse', ellipse)

cv2.waitKey(0)
And = cv2.bitwise_and(square, ellipse)
cv2.imshow('And', And)

cv2.waitKey(0)
OR = cv2.bitwise_or(square, ellipse)
cv2.imshow('Or', OR)

cv2.waitKey(0)
xor = cv2.bitwise_xor(square, ellipse)
cv2.imshow('Xor', xor)

cv2.waitKey(0)
Not = cv2.bitwise_not( ellipse)
cv2.imshow('not', Not)

cv2.waitKey(0)
cv2.destroyAllWindows()