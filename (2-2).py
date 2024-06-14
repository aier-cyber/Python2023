import argparse


parser = argparse.ArgumentParser(description = 'Write path to input & output')
parser.add_argument('pathTo_in', type = str, help = 'Where is matrix stored')
parser.add_argument('pathTo_out', type = str, help = 'Where is to leave ans')
args = parser.parse_args()

# Считывание матриц оформлено точно так же, как в matrix_mult
f = open(args.pathTo_in)
counter = 0

fst_matrix = []
str_Interpretation = f.readline()
while (not (str_Interpretation == "\n")):
    fst_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
    str_Interpretation = f.readline()
    
snd_matrix = []
str_Interpretation = f.readline()
while True:
    acc_len = len(str_Interpretation)
    if not (str_Interpretation[acc_len-1] == '\n'):
        snd_matrix.append(list(map(int, str_Interpretation.split(' '))))
        break
    snd_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
    str_Interpretation = f.readline()
    
f.close()

f = open(args.pathTo_out, 'w')
#                   0000
# пусть есть марица 0000 и ядро +0 - если просто вычесть длины по высоте и 
#                   0000        00                   ++00
# глубине, получится высота и глубина такого кусочка 0000, а мы ищем куда
#                                +++0                0000
# может вместиться ядро, то есть +++0 , Именно Поэтому прибавляем еденицу
#                                0000. 
# А так как нумерация начинается с нуля, берём строгое равенство когда
# рассматриваем координаты a и b
ans_deep = len(fst_matrix) - len(snd_matrix) + 1
ans_len = len(fst_matrix[0]) - len(snd_matrix[0]) + 1
# Соотвественно, работать будем отталкиваясь от уголка ядра - при координате
# (а,b) (где b - глубина) отсчитываем snd_matrix_deep+b-1 'вниз' и
# snd_matrix_len+a-1 'вправо' (-1 появляется из-за того, что покрытие ядром 
# считается прямо с клетки (a,b) - по сути тут будет клетка [0, 0] ядра)
print(ans_deep,' ', ans_len)
b = 0
snd_matrix_deep = len(snd_matrix)
snd_matrix_len = len(snd_matrix[0])
while (b < ans_deep):
    a = 0
    while(a < ans_len):
        curr_sum_of_mult = 0
        # Так как range не рассматривает крайнее значение, что бы 'зайти' в
        # b+snd_matrix_deep-1 надо брать до b+snd_matrix_deep-1+1
        # По пройденным координатам умножаем соответствующие числа в главной
        # матрице и ядре, и кидаем в curr_sum_of_mult, который можно сразу
        # вывести, так как файл уже открыт
        for i_b in range(b, b+snd_matrix_deep):
            for i_a in range(a, a+snd_matrix_len):
                print(i_a,' ', i_b)
                acc = snd_matrix[i_b-b][i_a-a]
                curr_sum_of_mult += fst_matrix[i_b][i_a]*acc
        f.write(str(curr_sum_of_mult))
        f.write(' ')
        a += 1
    f.write('\n')
    b += 1
f.close()
# Разбор крайних значений: (i_b < b+snd_matrix_deep) вложено в (b < ans_deep) 
# <=> b_max = ans_deep-1 + snd_matrix_deep-1 = 
# len(fst_matrix) - len(snd_matrix) + 1 - 1 + len(snd_matrix) - 1 =
# len(fst_matrix) - 0 + 1 - 1 - 1 = len(fst_matrix) - 1, отнимаем 1 из-за 
# нумерации с нуля. Аналогично с a