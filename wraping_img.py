import cv2
import numpy as np

path = "Resorses/box.png"
img = cv2.imread(path)

width , height = 400 , 400
pt1 = np.float32([[307,132],[465,150],[465,407],[307,353]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgwarped = cv2.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    img = cv2.circle(img, (int(pt1[x][0]), int(pt1[x][1])), 5, (255, 0, 0), cv2.FILLED)

cv2.imshow("Box",img)
cv2.imshow("wrap_box",imgwarped)
cv2.waitKey(0)