import cv2
import math
import numpy as np

file_src="car.jpg"

img_src=cv2.imread(file_src,1)

gamma=2.0
Y=np.ones((256,1),dtype="uint8")*0
for i in range(256):
    Y[i][0]=255*pow(float(i)/255,1.0/gamma)
img_dst=cv2.LUT(img_src,Y)

cv2.imwrite('car_gamma.png', img_dst)

#6-3-4 ネガポジ変換

img_dst2=255-img_src
cv2.imwrite('car_negaposi.png', img_dst2)
