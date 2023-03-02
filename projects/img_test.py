# first open cv testing

import cv2
image = cv2.imread("projects\sample.jpg")
h,w = image.shape[:2]
print(h,w)
b,g,r = image[100,100]
print(r,g,b)