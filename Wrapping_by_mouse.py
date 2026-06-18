import cv2
import numpy as np

cnt = 0
crl = np.zeros((4,2),np.int32)
def mouse(event, x, y, flags ,parameters):
    global cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        crl[cnt] = x, y
        cnt += 1
        print(crl)


path = "Resorses/box.png"
img = cv2.imread(path)
while True:
    if cnt == 4:
        width , height = 250 , 350
        pt1 = np.float32([crl[0],crl[1],crl[2],crl[3]])
        pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pt1,pt2)
        imgwarped = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("wrap_box",imgwarped)

    for x in range(0,4):
        img = cv2.circle(img, (int(crl[x][0]), int(crl[x][1])), 5, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Box",img)
    cv2.setMouseCallback("Box", mouse)
    cv2.waitKey(0)