import numpy as np
import random
import argparse
def random_selection(first, second, p):
    # На этот раз можно применить то, что скорее всего подразумевалось 
    # задачей - если в numpy.where после условия передать два массива,
    # при выполнении условия будет взят элемент из первого массива,
    # при невыполнении - из второго, и если в самом условии будет массив
    # той же размерности, генерироваться вывод будет поэлементно.
    arrnd = np.random.sample(first.size)
    # - так можно создать соразмерный с first массив случайных чисел от 0 до 1.
    # Так, если случайно сгенерированное число меньше, чем p, будем брать на ту
    # же ячейку элемент из синтетического массива, если больше - из реального 
    ans = np.where(arrnd <= p, second, first)
    return ans


# Ниже всё как в первом варианте с точностью до слова
parser = argparse.ArgumentParser(description = 'Write path to input & output')
parser.add_argument('pathTo_in_one', type = str, help = 'Where is first arr')
parser.add_argument('pathTo_in_two', type = str, help = 'Where is second arr')
parser.add_argument('P_robability', type = str, help = 'Chance to take *false* data')
args = parser.parse_args()
#
f = open(args.pathTo_in_one)
str_Interpretation = f.readline()
array_list_type = str_Interpretation.split(' ')
first_arr = np.array(list(map(int,array_list_type)))
f.close()
#
f = open(args.pathTo_in_two)
str_Interpretation = f.readline()
array_list_type = str_Interpretation.split(' ')
second_arr = np.array(list(map(int,array_list_type)))
f.close()
#
answer = random_selection(first_arr, second_arr, float(args.P_robability))
print(answer)