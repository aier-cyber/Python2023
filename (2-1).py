import argparse


parser = argparse.ArgumentParser(description = 'Write path to input & output')
parser.add_argument('pathTo_in', type = str, help = 'Where is matrix stored')
parser.add_argument('pathTo_out', type = str, help = 'Where is to leave ans')
args = parser.parse_args()


f = open(args.pathTo_in)
counter = 0
# Чтобы не работать сразу со всем файлом, будем считывать по строке из файла
# Считаем первую матрицу, до строки "\n" (эта строка и разделяет матрицы)
fst_matrix = []
str_Interpretation = f.readline()
while (not (str_Interpretation == "\n")):
    # Строки у нас вида "1 2 3\n", то есть надо отделить от последней цифры
    # знак переноса строки (это оформлено как [0:-1]), разбить по пробелу,
    # что равносильно "убрать пробелы", получившиеся цифры ("символьные") 
    # закастить к инту, и получившийся map объект 'вернуть' в список.
    # Затем добавить в результат (изначально пустой список) с помощью append
    fst_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
    str_Interpretation = f.readline()
# Вторая матрица считана аналогично, только считываем уже не до знака переноса
# строки, а до конца файла - из-за этого нужно контроллировать, когда взята
# строчка с переносом строки, а когда нет, иначе теряется элемент матрицы
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


# Теперь будем проходить по строкам первой матрицы, и уже будучи внутри строк 
# умножать на числа столбцов второй матрицы и складывать с общим ответом ячейки
# (sum_mult), получая соотвествующую ячейку. С помощью write
# можно записывать данные в out сразу после подсчёта ячейки
# (! Алгоритм не поддерживает вырожденное умножение - количество столбцов
# первой матрицы должно быть равно количеству строк второй матрицы !)
f = open(args.pathTo_out, 'w')
for current in fst_matrix:
    snd_matrix_column = 0
    while (snd_matrix_column < len(snd_matrix[0])):
        matrix_deep = 0
        sum_mult = 0
        for fst in current:
            snd = snd_matrix[matrix_deep][snd_matrix_column]
            sum_mult += fst * snd
            matrix_deep += 1
        f.write(str(sum_mult))
        f.write(' ')
        snd_matrix_column += 1
    f.write('\n')
f.close()
#
#
#
#
#
#