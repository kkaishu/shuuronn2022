import cv2
import math
import numpy as np

from numpy import dtype

file_src="car.jpg"
img_src=cv2.imread(file_src,1)

img_dst=cv2.Canny(img_src,100,200)
# 第1引数：入力画像、
# 第2,3引数：ヒステリシスを使ったしきい値処理に使う minVal と maxVal 
cv2.imwrite('car_Canny_edge_detection.png', img_dst)
