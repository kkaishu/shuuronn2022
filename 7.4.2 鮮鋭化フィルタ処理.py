import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)


k=1.0
op=np.array([[-k,-k,   -k],
             [-k,1+8*k,-k],
             [-k,-k,   -k]])


img_tmp=cv2.filter2D(img_src,-1,op)
# Sobel:任意オペレータを画像に適用。
# 第1引数：入力画像、第2引数：出力画像のbit深度。負の場合は入力画像と同じ、
# 第3引数：オペレータ

img_dst=cv2.convertScaleAbs(img_tmp)
# convertScaleAbs:スケーリングを行う
# 第1引数：入力画像、
cv2.imwrite('car_Sharpening.png', img_dst)
