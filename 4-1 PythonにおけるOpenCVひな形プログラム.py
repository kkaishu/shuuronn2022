#教科書P52


import cv2
import math
import numpy as np

file_src="car.jpg"
file_dst="dst.png"

img_src=cv2.imread(file_src,1)

# cv2.namedWindow("src")
cv2.namedWindow("dst")

img_dst=cv2.flip(img_src,flipCode=0)

cv2.namedWindow("src", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('src', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("src",img_src)
cv2.imshow("dst",img_dst)
cv2.imwrite('car_2.png', img_src)
cv2.imwrite(file_dst,img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()





