import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

img_tmp=cv2.Sobel(img_src,cv2.CV_32F,1,0)
# Sobel:微分画像を求める。
# 第1引数：入力画像、第2引数：出力画像のbit深度、
# 第3引数：xに関する微分の次数、第4引数：yに関する微分の次数

img_dst=cv2.convertScaleAbs(img_tmp)
# convertScaleAbs:スケーリングを行う
# 第1引数：入力画像、
cv2.imwrite('car_Sobel_edge_detection.png', img_dst)
