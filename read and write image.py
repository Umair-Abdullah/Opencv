import cv2

img = cv2.imread('my.jpg')

cv2.imshow('orignal',img)

#cv2.imwrite('img1.png',img)
#cv2.imwrite('img2.jpg',img)

#To convert image into grayscale

# cv2.waitKey(0)
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)

#To convert image into binary

cv2.waitKey(0)
img = cv2.imread('my.jpg',0)
cv2.imshow('gyar',img)

cv2.waitKey(0)
ret, bw= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('black',bw)

#To convert image into HSV
cv2.waitKey(0)
img=cv2.imread('my.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()