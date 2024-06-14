import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Создадим аналоги зелёного и красного цветов  
green = np.array([0, 255, 0], dtype = np.uint8)
red = np.array([0, 0, 255], dtype = np.uint8)
# Использован вариант для чтения файла
main_path = input()
cap = cv2.VideoCapture(main_path)
Prev = None
while(1):
    ret, img_bgr = cap.read()
    if (ret == True):
# GaussianBlur - способ избавиться от шумов, описанный в 7-й лекции
        prepared_frame = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2GRAY)
        prepared_frame = cv2.GaussianBlur(prepared_frame, ksize = (5, 5), sigmaX = 8)
        if (Prev is None):
            Prev = prepared_frame
            continue
# Чтобы найти изменения, используем absdiff
        diff = cv2.absdiff(Prev, prepared_frame)
        kernel = np.ones([5,5])
        diff = cv2.dilate(diff, kernel, 1)    
        diff_r = cv2.cvtColor(diff, cv2.IMREAD_COLOR)
# Теперь надо поменять цвета. Я сделал это с помощью np.where. В сравнение 
# берётся ячейка из diff_r, тип которого был возвращён к трёхканальному,
# и если соответствующаяя ячейка достаточно тёмная (чёрный цвет означает,
# что движения небыло - думаю важно заметить, что если показатель будет
# меньше, будут улавливаться даже малейшие изменения, равносильно отображению
# абсолютно всех шумов), цвет меняется на зелёный, иначе на красный
        mask = np.where(diff_r < (20, 20, 20), green, red)
# Настоящий кадр выводим в окошке Frame
        cv2.imshow('Frame', img_bgr)
# Изменения - в окошке change
        cv2.imshow('Change', mask)
        cv2.waitKey(20)
# Теперь предыдущим кадром становится текущий
        Prev = prepared_frame
    else:
        break
cv2.destroyWindow('Frame')
cv2.destroyWindow('Change')
#
#
#
#
#