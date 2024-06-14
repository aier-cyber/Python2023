import numpy as np
import random
import argparse
# Решил сделать именно такое решение из-за ассоциаций с задачей 4.1
def random_selection(first, second, p):
# Используя превращение из списка элементов к списку списков элементов и метода 
# numpy.hstack можно получить из двух массивов массив массивов по два элемента.
    # Возьмём первый массив, закастим к list чтобы можно было использовать map
    # (apply_along_axis не пойдёт - в np у одномерного массива один элемент),
    # и используя анонимную функцию, возвращающую список из одного элемента, 
    # создадим список списков, что в numpy понимании будет матрицей с одним
    # столбцом
    first_extended = list(map(lambda x: [x],list(first)))
    # Вернём к array виду (без этого нельзя использовать заветный hstack)
    fir_ex_np = np.array(first_extended)
    # То же самое со вторым массивом
    second_extended = list(map(lambda x: [x], list(second)))
    sec_ex_np = np.array(second_extended)
    # Склеиваем
    mix = np.hstack((fir_ex_np,sec_ex_np))
    # Делаем очередной map со следующей функцией;
    # Если условие верно, то есть сгенерировалось число меньшее или равное, чем
    # P, что равносильно тому, что мы попали в эту вероятность, берём число
    # из второго - синтетического массива. Иначе берём из первого.
    l_ans = list(map(lambda x: x[1] if (random.random() <= p) else x[0], list(mix)))
    ans = np.array(l_ans)
    return ans


parser = argparse.ArgumentParser(description = 'Write path to input & output')
parser.add_argument('pathTo_in_one', type = str, help = 'Where is first arr')
parser.add_argument('pathTo_in_two', type = str, help = 'Where is second arr')
parser.add_argument('P_robability', type = str, help = 'Chance to take *false* data')
args = parser.parse_args()

# Откроем оба файла
# Читаем строку, разбиваем по пробелу, кастим к инту, затем к np
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
# Передадим два получившихся массива в random_selection
answer = random_selection(first_arr, second_arr, float(args.P_robability))
print(answer)
#
#
#
#
#