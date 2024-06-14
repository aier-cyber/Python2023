# Pupa&Lupa
import random
#
# Оба Pupa и Lupa класса абсолютно идентичны, за исключением того, что Pupa 
# поэлементно суммирует, а Lupa поэлементно вычитает
class Pupa:
    def __init__(self):
        self.bank = 0
        self.confidence = 0
# Так как у обоих классов определён take_salary, вне зависимости от того, что
# будет передано give_salary - Pupa или Lupa, этот метод вызовется без ошибок
    def take_salary(self, salary: int):
        self.bank += salary
# Считывание матриц скопировано с уже отправленных мной matrix-скриптов.
# Единственное различие - матрицы записаны не в одном файле, поэтому считывание
# строк ведётся сразу до строки, в которой нет \n (после которой ничего нет)
    def do_work(self,filename1, filename2):
        fst_matrix = []
        snd_matrix = []
# Считываем первую матрицу
        f = open(filename1)
        counter = 0
        str_Interpretation = f.readline()
        while True:
            acc_len = len(str_Interpretation)
            if not (str_Interpretation[acc_len-1] == '\n'):
                fst_matrix.append(list(map(int, str_Interpretation.split(' '))))
                break
            fst_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
            str_Interpretation = f.readline()   
        f.close()
# Считываем вторую матрицу
        f = open(filename2)
        counter = 0
        str_Interpretation = f.readline()
        while True:
            acc_len = len(str_Interpretation)
            if not (str_Interpretation[acc_len-1] == '\n'):
                snd_matrix.append(list(map(int, str_Interpretation.split(' '))))
                break
            snd_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
            str_Interpretation = f.readline()   
        f.close()
# Далее идёт поэлементное сложение/вычитание с расширением. Если например 3х4 -
# размер первой матрицы, а второй - 4х3, то они будут нулями дополнены до 4x4
# (теоретически, не в программе), и соотвественно в ответе будет матрица 4х4.
# Pupa и Lupa достаточно хитрые, чтобы нехотеть выводить полную матрицу, 
# поэтому выводят полную матрицу они с шансом 10%. А вообще никто не 
# просил выводить не 3х3. Если же им всё-таки хватает сил сделать свою работу
# качественно, их confidence вырастает с 0 до 1 
        f_m_w = len(fst_matrix[0])
        s_m_w = len(snd_matrix[0])
        f_m_h = len(fst_matrix)
        s_m_h = len(snd_matrix)
        if (random.randint(1, 10) == 10):
            ans_wide = max(f_m_w, s_m_w)
            ans_hight = max(f_m_h, s_m_h)
            self.confidence = 1
        else:
            ans_wide = min(f_m_w, s_m_w)
            ans_hight = min(f_m_h, s_m_h)
        for y in range(0, ans_hight):
            show_helper = ''
            for x in range(0, ans_wide):
                if ((x < f_m_w) and (y < f_m_h)):
                    curr_f = fst_matrix[y][x]
                else:
                    curr_f = 0
                if ((x < s_m_w) and (y < s_m_h)):
                    curr_s = snd_matrix[y][x] 
                else:
                    curr_s = 0
                show_helper += str(curr_f+curr_s)
                if (x < ans_wide-1):
                    show_helper += ' '
            print(show_helper)


class Lupa:
    def __init__(self):
        self.bank = 0
        self.confidence = 0

    def take_salary(self, salary: int):
        self.bank += salary

    def do_work(self, filename1, filename2):
        fst_matrix = []
        snd_matrix = []
        # Считываем первую матрицу
        f = open(filename1)
        counter = 0
        str_Interpretation = f.readline()
        while True:
            acc_len = len(str_Interpretation)
            if not (str_Interpretation[acc_len-1] == '\n'):
                fst_matrix.append(list(map(int, str_Interpretation.split(' '))))
                break
            fst_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
            str_Interpretation = f.readline()   
        f.close()
        # Считываем вторую матрицу
        f = open(filename2)
        counter = 0
        str_Interpretation = f.readline()
        while True:
            acc_len = len(str_Interpretation)
            if not (str_Interpretation[acc_len-1] == '\n'):
                snd_matrix.append(list(map(int, str_Interpretation.split(' '))))
                break
            snd_matrix.append(list(map(int, str_Interpretation[0:-1].split(' '))))
            str_Interpretation = f.readline()   
        f.close()
        # Вычитаем
        f_m_w = len(fst_matrix[0])
        s_m_w = len(snd_matrix[0])
        f_m_h = len(fst_matrix)
        s_m_h = len(snd_matrix)
        if (random.randint(1, 10) == 10):
            ans_wide = max(f_m_w, s_m_w)
            ans_hight = max(f_m_h, s_m_h)
            self.confidence = 1
        else:
            ans_wide = min(f_m_w, s_m_w)
            ans_hight = min(f_m_h, s_m_h)
        for y in range(0, ans_hight):
            show_helper = ''
            for x in range(0, ans_wide):
                if ((x < f_m_w) and (y < f_m_h)):
                    curr_f = fst_matrix[y][x]
                else:
                    curr_f = 0
                if ((x < s_m_w) and (y < s_m_h)):
                    curr_s = snd_matrix[y][x] 
                else:
                    curr_s = 0
                show_helper += str(curr_f-curr_s)
                if (x < ans_wide-1):
                    show_helper += ' '
            print(show_helper)


class Accountant:
    def __init__(self):
        pass
    
    def give_salary(self, worker):
        worker.take_salary(15000)
# После того, как бухгалтеру удаётся заставить Pupa или Lupa работать, в 
# зависимости от того, сдали они работу с уверенностью в глазах, или же
# с хитро ускользающим в пол взглядом, бухгалтер, если ничего не перепутал,
# даёт премию. Если же бухгалтер всё перепутает, то с шансом 10% работник
# вместо премии получит ничего, и его зарплата уйдёт кому-то другому. То есть
# есть шанс 1% что лупа получит за пупу, а пупа за... ничего не получит
    def go_work_bum(self, worker, file_one, file_two):
        worker.do_work(file_one, file_two)
        if (worker.confidence == 1):
            if (random.randint(1, 10) != 10):
                self.give_salary(worker)
                self.give_salary(worker)
            worker.confidence = 0
        else:
            self.give_salary(worker)
"""
# tests:
cpp_master = Pupa()
assembler_virtuoso = Lupa()
python_enjoyer = Accountant()
filename = input() # путь к первой матрице
s_filename = input() # путь к второй матрице
python_enjoyer.go_work_bum(cpp_master, filename, s_filename)
print("checking bank: ", cpp_master.bank)
print("more!!!")
python_enjoyer.go_work_bum(cpp_master, filename, s_filename)
print("more!!!")
python_enjoyer.go_work_bum(cpp_master, filename, s_filename)
print("checking bank: ", cpp_master.bank)
python_enjoyer.go_work_bum(assembler_virtuoso, filename, s_filename)
print("more!!!")
python_enjoyer.go_work_bum(assembler_virtuoso, filename, s_filename)
print("checking bank: ", cpp_master.bank)
"""
#
#
#
#
#