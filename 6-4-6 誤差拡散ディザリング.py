import cv2
import numpy as np
import random as rand


file_cat = 'car.jpg'

color = cv2.imread(file_cat , 1) 
gray = cv2.imread(file_cat , 0) #グレースケール

height, width = gray.shape # 高さ・幅取得

thresh = 128 # 閾値
gosa = 0 # 誤差

for i in range(height):
    for j in range(width):
        if gray[i][j] + gosa < thresh:
            gosa = gray[i][j] + gosa - 0 # 誤差を計算
            gray[i][j] = 0
        else:
            gosa = gray[i][j] + gosa - 255 # 誤差を計算
            gray[i][j] = 255


cv2.imwrite('car_Error_diffusion_dithering.png', gray)
