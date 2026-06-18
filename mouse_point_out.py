import cv2
import numpy as np

def mouse(event, x, y, flags ,parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img = cv2.imread("Resorses/box.png")
cv2.imshow("box",img)
cv2.setMouseCallback("box",mouse)
cv2.waitKey(0)