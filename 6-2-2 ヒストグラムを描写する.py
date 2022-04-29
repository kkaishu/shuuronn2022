# 教科書p76

import cv2
import math
import numpy as np

file_src="car.jpg"
# file_dst="dst.png"

img_src=cv2.imread(file_src,1)#グレースケールの場合は0
# ヒストグラム均一化
# img_src = cv2.equalizeHist(img_src)

#ここから新規

import itertools

img_hst = np.zeros([100,256]).astype("uint8")
rows,cols = img_hst.shape[:2]

hdims = [256]
hranges = [0,256]
hist = cv2.calcHist([img_src],[0],None,hdims,hranges)
# print(hist)

min_val,max_val,min_loc,max_loc =cv2.minMaxLoc(hist)
# histは二重リスト型で格納されているので、一元化する
hist_h = list(itertools.chain.from_iterable(hist))
# print(hist_h)

for i in range(0,255):
    v = hist_h[i]
    # print(rows-rows*(v/max_val))
    # cv2.lineメソッドとcv2.circleメソッドの引数は、int型である必要がある。
    # この制約を満たすために、座標点が整数値(integer）になるように、int()で型変換する。
    cv2.line(img_hst,(i,rows),(i,int(rows-rows*(v/max_val))),(255,255,255))

# car_histgram.pngとして、保存する。
cv2.imwrite('car_histogram.png', img_hst)

