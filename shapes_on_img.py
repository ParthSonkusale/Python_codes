import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[:] = 0,255,0 make the blank img colour in BGR or others

img = cv2.line(img,(0,0),(img.shape[1] , img.shape[0]),(255,0,0),3)
img = cv2.rectangle(img,(350,100),(450,200),(50,10,255),2)
img = cv2.circle(img,(150,400),50,(30,0,50),2)
img = cv2.putText(img,"Hi i am Parth",(70,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('blank_img',img)
cv2.waitKey(0)
