import cv2

img = cv2.imread('Resorses/harsh.jpg')
print(img.shape)
imgresize = cv2.resize(img,(220,140))
imgcrop   = img[0:80,100:200,]#(y,x)
imgcrop_resize = cv2.resize(imgcrop,(img.shape[1],img.shape[0]))
cv2.imshow('img crop re',imgcrop_resize)
cv2.imshow('img crop',imgcrop)
cv2.imshow('img resize',imgresize)
cv2.imshow('img',img)
cv2.waitKey(0)