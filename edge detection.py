import cv2
import numpy as np

# read the image and convert in grayscale
img = cv2.imread('my.jpg', 0)
cv2.imshow('original', img)

# height = h & width = w
h, w = img.shape
# Sobel method
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.waitKey(0)
cv2.imshow('sobel x' , sobel_x)

cv2.waitKey(0)
cv2.imshow('sobel y', sobel_y)

cv2.waitKey(0)
sobel_xy = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel xy', sobel_xy)

# Laplacian method
cv2.waitKey(0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)

# canny method
cv2.waitKey(0)
canny = cv2.Canny(img, 100, 200)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()