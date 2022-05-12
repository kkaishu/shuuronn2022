import cv2
import numpy as np
import random as rand

file_cat = 'car.jpg'

color = cv2.imread(file_cat , 1) 
gray = cv2.imread(file_cat , 0) #グレースケール

height, width = gray.shape # 高さ・幅取得

for i in range(height):
    for j in range(width):
        if gray[i][j] < rand.randint(0,255):
            gray[i][j] = 0
        else:
            gray[i][j] = 255
            
cv2.imwrite('car_Random_dithering.png', gray)



