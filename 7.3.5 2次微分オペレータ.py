import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

img_tmp=cv2.Laplacian(img_src,cv2.CV_32F,3)
# Sobel:画像の2次微分を求める。
# 第1引数：入力画像、第2引数：出力画像のbit深度、
# 第3引数：オペレータのサイズ

img_dst=cv2.convertScaleAbs(img_tmp)
# convertScaleAbs:スケーリングを行う
# 第1引数：入力画像、
cv2.imwrite('car_Second_derivative_operator.png', img_dst)
