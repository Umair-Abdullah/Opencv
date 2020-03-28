import cv2
import numpy as np

img = cv2.imread('my.jpg')
cv2.imshow('orignal',img)
#
# cv2.waitKey(0)
# s_img=cv2.resize(img,None,fx=0.5,fy=0.5)
# cv2.imshow('resize',s_img)
#
# cv2.waitKey(0)
# l_img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# cv2.imshow('large image',l_img)

# cv2.waitKey(0)
# a_img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_NEAREST)
# cv2.imshow('area',a_img)
h,w = img.shape[:2]
print(h,w)

s_row, s_col = int(h*0.38),int(w*0.40)
e_row,e_col= int(h*0.82),int(w*0.75)

c_img=img[s_row:e_row,s_col:e_col]
cv2.imshow('cropped',c_img)
cv2.waitKey(0)
cv2.destroyAllWindows()