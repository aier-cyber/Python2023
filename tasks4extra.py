import numpy as np
import random
# 2

h_eight = int(input())
w_idth = int(input())
b = np.arange(0,256)
# За каждый канал будут отвечать массивы red, green и blue соотвественно. 
red = np.array(np.random.choice(b, (w_idth,h_eight)), dtype=np.uint8)
green = np.array(np.random.choice(b, (w_idth,h_eight)), dtype=np.uint8)
blue = np.array(np.random.choice(b, (w_idth,h_eight)), dtype=np.uint8)
# Для подсчёта уникальных значений необязательно сохранять слоям двухмерную
# форму - можно сложить всё как вектора и посчтитать уникальные тройки.
vec_red = red.ravel()
vec_blue = blue.ravel()
vec_green = green.ravel()
rgb_stat = np.stack((vec_red,vec_blue,vec_green), axis = -1)
print(len(np.unique(rgb_stat, axis = 0)))

# 3

# На этот раз вычислял как "Простое скользящее среднее" для сглаживающего 
# интервала = 3 
ar = np.random.randint(5, size = 10)
acc = np.arange(0,len(ar))
# Мапаем по функции: cписок из трёх подряд идущих элементов либо если точка 
# крайняя - пустой список
slipper = list(map(lambda x: [ar[x-1],ar[x],ar[x+1]] if ((x != 0) and (x != len(acc)-1)) else [], acc))
# Удаляем пустые списки
slipper = slipper[1:len(slipper)-2]
# Мапаем по функции: среднее значение трёхэлементного подсписка, кастим к аrray
slip_avg = np.array(list(map(lambda x: (x[0]+x[1]+x[2])/3, slipper)))
avg = slip_avg.sum()/len(slip_avg)
print(avg)
