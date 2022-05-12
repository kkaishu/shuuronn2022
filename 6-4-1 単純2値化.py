import cv2
import numpy as np

file_cat = 'car.jpg'

color = cv2.imread(file_cat , 1) 

#gray = cv2.cvtColor(file_cat, cv2.COLOR_BGR2GRAY) #グレースケール化
gray = cv2.imread(file_cat , 0) #グレースケール
height, width = gray.shape # 高さ・幅取得
# print(height,width)
thresh = 128 # 閾値

for i in range(height):
    for j in range(width):
        
        if gray[i][j] < thresh: # 閾値未満なら黒
            gray[i][j] = 0
            
        else: # 白色
            gray[i][j] = 255
 
cv2.imwrite('car_Simple_binarization.png', gray)