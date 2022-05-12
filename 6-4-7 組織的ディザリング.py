import cv2
import numpy as np
import random as rand

file_cat = 'car.jpg'

gray = cv2.imread(file_cat , 0) #グレースケール

height, width = gray.shape # 高さ・幅取得

# ディザリング表
matrix = [[0, 8, 2, 10],[12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


for i in range(4):
    for j in range(4):
        matrix[i][j] = matrix[i][j] * 16

for i in range(height):
    for j in range(width):
        if gray[i][j] < matrix[i % 4][j % 4]: # 4区切りずつ判定する
            gray[i][j] = 0
            
        else:
            gray[i][j] = 255
            
cv2.imwrite('car_Organizational_dithering.png', gray)
