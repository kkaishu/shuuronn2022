import cv2
import math
import numpy as np

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

shift=100
table=np.arange(256,dtype=np.uint8)
for i in range(0,255):
    j=i+shift
    if j<0:
        table[i]=0
    elif j>255:
        table[i]=255
    else:
        table[i]=j

img_dst=cv2.LUT(img_src,table)
cv2.imwrite('car_brightness.png', img_dst)