import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

min=100
max=200
table=np.arange(256,dtype=np.uint8)
for i in  range(0,255):
    table[i]=min+i*(max-min)/255

img_dst=cv2.LUT(img_src,table)

#方法2
# cv2.normalize(img_src,img_dst,min,max,cv2.NORM_MINMAX)

cv2.imwrite('car_contrast_reduction.png', img_dst)