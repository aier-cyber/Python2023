import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


green = np.array([0, 255, 0], dtype = np.uint8)
red = np.array([0, 0, 255], dtype = np.uint8)
main_path = input()
cap = cv2.VideoCapture(main_path)
Prev = None
acc = 0
while(1):
# Для симуляции таймера добавим acc, увеличивающийся на значение внутри WaitKey
# Если acc от 0 до 1000, будет происходить проверка изменений, от 1000 до 2000 
# - не будет, а если acc == 2000 - обнуление acc
# На практике оказалось, что из-за времени выполнения верхней ветки время
# проверки/не проверки распределено неравномерно, поэтому waitkey в нижней ветке
# больше, при этом acc там же всё равно меняется на 20. 
    if (acc == 2000):
        acc = 0
    ret, img_bgr = cap.read()
    if (ret == True):
        if (acc < 1000):
            prepared_frame = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2GRAY)
            prepared_frame = cv2.GaussianBlur(prepared_frame, ksize = (5, 5), sigmaX = 8)
            if (Prev is None):
                Prev = prepared_frame
                continue
            diff = cv2.absdiff(Prev, prepared_frame)
            kernel = np.ones([5,5])
            diff = cv2.dilate(diff, kernel, 1)    
            diff_r = cv2.cvtColor(diff, cv2.IMREAD_COLOR)
            mask = np.where(diff_r < (20, 20, 20), green, red)
# Чтобы наложить маску на изображение, используется addWeighted
            masked = cv2.addWeighted(img_bgr, 0.8, mask, 0.6, 0)
# Добавление текста 
            cv2.putText(masked, 'Do not move', (0, len(masked)-1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Frame', masked)
            acc += 20
            cv2.waitKey(20)
            Prev = prepared_frame
        else:
            prepared_frame = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2GRAY)
            prepared_frame = cv2.GaussianBlur(prepared_frame, ksize = (5, 5), sigmaX = 8)
            cv2.putText(img_bgr, 'Move', (0, len(masked)-1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Frame', img_bgr)
            acc += 20
            cv2.waitKey(40)
            Prev = prepared_frame
    else:
        break
cv2.destroyWindow('Frame')
#
#
#
#
#