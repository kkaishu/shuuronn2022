import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

min=150
max=200
table=np.arange(256,dtype=np.uint8)
for i in range(0,min):
    table[i]=0
for i in range(min,max):
    table[i]=255*(i-min)/(max-min)
    table[i]=255

img_dst=cv2.LUT(img_src,table)
cv2.imwrite('car_contrast_enhancement.png', img_dst)