import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

img_dst=cv2.GaussianBlur(img_src,(11,11),1)
# 第1引数：入力画像、第2引数：オペレータのサイズ、
# 第3引数：Gaussianオペレータのx軸方向の標準偏差σ、第4引数：Gaussianオペレータのy軸方向の標準偏差σ
img_dst2=cv2.bilateralFilter(img_src,11,50,100)
# 第1引数：入力画像、第2引数：オペレータのサイズ、
# 第3引数：色空間に関する標準偏差σ2、第4引数：距離空間に関する標準偏差σ1

# 第一引数：入力画像、第二引数：オペレータのサイズ
cv2.imwrite('car_Gaussian_operator.png', img_dst)
cv2.imwrite('car_Bilateral_operator.png', img_dst2)
