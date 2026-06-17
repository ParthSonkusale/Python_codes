# -*- coding: utf-8 -*-
"""
Created on Sun May 24 07:48:14 2026

@author: user
"""

import cv2
img = cv2.imread('blur_images.png')
clahe = cv2.createCLAHE()
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img = clahe.apply(gray_img)
cv2.imwrite('enhanced.png',enh_img) 
print("successfully enhanced")