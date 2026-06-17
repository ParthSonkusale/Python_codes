import cv2
import numpy as np

kernal = np.ones((5,5), np.uint8)#matrix of 5*5,u-unsigned ,int - integer,8 - use8bitmemory,ones = fill all n*m with 1

img = cv2.imread("Resorses/harsh.jpg")
imgblur = cv2.GaussianBlur(img,(9,9),0)#the (5,5)is the intensity of the blurness and it can be only odd no.
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgcanny=cv2.Canny(imggray,100,200) # it give only edges on the image
imgdilation = cv2.dilate(imgcanny,kernal, iterations = 1)# it increase the width of img edge it = 2 , 3 , 4, 5

cv2.imshow('harsh',img)
cv2.imshow('harsh_gray',imggray)
cv2.imshow('harsh_blur',imgblur)
cv2.imshow('harsh_canny',imgcanny)
cv2.imshow('harsh_dilation',imgdilation)
cv2.waitKey(0)