import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

img_dst=cv2.medianBlur(img_src,9)
# 第一引数：入力画像、第二引数：フィルタのサイズ
cv2.imwrite('car_Median_filtering.png', img_dst)
