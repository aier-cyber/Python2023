import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
# 1-3 

ft_path = input()
sd_path = input()
#ft_path = "nails_segmentation/images"
#sd_path = "nails_segmentation/labels"
for image in os.listdir(ft_path):
    for label in os.listdir(sd_path):
# Смотрим совпадает ли название картинок
        if (image == label):
# Создаём путь до картинок и читаем их
            path_1 = os.path.join(ft_path, image)
            image_real = cv2.imread(path_1)
            path_2 = os.path.join(sd_path, label)
            label_real = cv2.imread(path_2)
# Перед выводом отрисуем контуры на основном изображении (6.3). Чтобы поиск
# контуров работал пришлось поменять цвет на серый, затем сделать бинаризацию
# (махинации по лекции). Если цвет не серый жалуется на тип, если оставить 
# просто серым очень много шумов.
            label_gray = cv2.cvtColor(label_real, cv2.COLOR_RGB2GRAY)
            _, l_g_bin = cv2.threshold(label_gray, 200, 255, cv2.THRESH_BINARY)
            kntr, hierarc = cv2.findContours(l_g_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            image_real = cv2.drawContours(image_real, kntr, -1, (0, 255, 0), 2)
# Чтобы вывести оба изображения в одном окне (6.2), объединим их, для чего
# придётся сшить rgb-уровни. Это напрямую делает hstack из numpy
            output_image = np.hstack((image_real,label_real))
# Вывод ответа в окно с ожиданием нажатия для переключения 
            cv2.imshow('Wndw', output_image)
            cv2.waitKey(0)
            cv2.destroyWindow('Wndw')

#4

vid_path = input()
# Считывание видео так же, как в лекции, за исключением того, что проверка 
# ret внутри цикла (чтобы imshow не пытался создать окно с null-фреймом)
cap = cv2.VideoCapture(vid_path)
while(1):
    ret, frame = cap.read()
    if (ret == True):
# Перевод в градации серого
        image_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Frame', image_gray)
        cv2.waitKey(50)
    else:
        break
cv2.destroyWindow('Frame')
cap.release()

#
#
#
#
#