import numpy as np
import pandas as pd
import datetime


def task_f(row, rwmax: int, ldmed: float):
# Меняем М/м/Ж/ж на 1, всё остальное - на 0 (5.1) 
    x = row['sex']
    if ((x == 'M') or (x == 'м') or (x == 'Ж') or (x == 'ж')):
        row.at['sex'] = 1
    else:
        row.at['sex'] = 0
# Если в row_number было NAN, меняем на max (5.2)
    if (np.isnan(row.at['row_number'])):
        row.at['row_number'] = rwmax
# Если в liters_drunk значение меньше 0 или больше 5, меняем на среднее (5.3)
    if ((row.at['liters_drunk'] < 0) or (row.at['liters_drunk'] > 5)):
        row.at['liters_drunk'] = ldmed
# Если в названии напитка присутствовало 'beer', напиток хмельный (5.5)
    if ((row.at['drink']).rfind('beer') == (-1)):
        row.at['drink'] = 0
    else:
        row.at['drink'] = 1
    return row
# time_fun меняет значения в новых колонках age_... в зависимости от значения
# в age и так же с периодом дня сеанса.
def time_fun(row):
    if (row.at['age'] < 18):
        row.at['age_kid'] = '+'
    elif(row.at['age'] < 50):
        row.at['age_adult'] = '+'
    else:
        row.at['age_old'] = '+'
    
    v_time = pd.to_datetime(row.at['session_start'])
    if (v_time < pd.to_datetime('12:00:00')):
        row.at['morning'] = '+'
    elif (v_time < pd.to_datetime('18:00:00')):
        row.at['day'] = '+'
    else:
        row.at['evening'] = '+'
    return row


t_w_l_way = input()
c_s_way = input()
# c_s_way = "cinema_sessions.csv"
# t_w_l_way = "titanic_with_labels.csv"
# Буквы 'Ж' и 'м' - это кириллица. Параметр encoding = 'cp1251'
# позволяет читать кириллицу... Но это не точно. Sep отвечает за разделитель,
# обычно это запятая, но в предложенных файлах это пробел. Во втором файле 
# кириллицы нет, так что и encoding пропущен.
twl = pd.read_csv(t_w_l_way, sep = ' ', index_col = 0, encoding = 'cp1251')
cs = pd.read_csv(c_s_way, sep = ' ', index_col = 0)
# Получим максимальное значение в row_number и среднее значение liters_drunk
task_two = int(max(twl['row_number']))
task_three = twl['liters_drunk'].mean()
# Применяем task_f 
step_one = twl.apply(lambda x: task_f(x,task_two,task_three), axis = 1)
# С помощью merge по индексам chcek_number добавим session_start для (5.6)
step_two = pd.merge(step_one, cs, on = 'check_number')
# Добавим 3 колонки под каждый из возрастов, изначально '-', под задачу (5.4)
step_two['age_kid'] = '-'
step_two['age_adult'] = '-'
step_two['age_old'] = '-'
# Затем добавим 3 колонки под время сеанса (5.6)
step_two['morning'] = '-'
step_two['day'] = '-'
step_two['evening'] = '-'
# Применим функцию time_fun
step_three = step_two.apply(time_fun, axis = 1)
# Удалим колонку age
step_three.drop('age', axis=1).columns
# Вывод ответа?
# print(step_three)
#
#
#
#
#