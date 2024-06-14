import numpy as np
import pandas as pd
import datetime
# 1

data = np.random.random(size=(10, 5))
df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e'])
# С помощью applymap обнуляем во всей таблице элементы, меньшие 0.3
df2 = df.applymap(lambda x: 0 if (x < 0.3) else x)
# Теперь складываем все значения в каждой строке, сразу делим на кол-во 
# элементов, и выводим 
df2.apply(lambda x: print(sum(x)/len(x)), axis = 1)

# 2

# За месяц взято 30 дней, считаются дни (ответ довольно точный)
def fun(row):
    start_date = pd.to_datetime(row['SpudDate'])
    end_date = pd.to_datetime(row['CompletionDate'])
    print((end_date - start_date).days//30)
# way - это путь до "wells_info.csv"
way = input()
# way = "data/wells_info.csv"
df = pd.read_csv(way)
df.apply(fun, axis = 1)

# 3

way = input()
df = pd.read_csv(way)
df_stats = df.describe()
# С помощью df.apply и value_counts можно получить количество каждого элемента 
# для каждой строки. Пройдя по столбцам получившейся таблицы можно найти  
# наиболее встречаймое значение изначальной таблицы, просто посчитав сумму
prop = df.apply(lambda x: x.value_counts(), axis = 1)
changer = None
changer_max = 0
for y in prop.columns:
    if (changer_max < prop[y].sum()):
        changer_max = prop[y].sum()
        changer = y
# Теперь рассмотрев тип колонки можно понять, на какой элемент заменять None
for x in df.columns:
    if (df.dtypes[x] == object):
        for i in range(0, len(df[x])):
            if (pd.isnull(df.loc[i, x])):
                df.loc[i, x] = changer
    else:
        for i in range(0, len(df[x])):
            if (pd.isnull(df.loc[i, x])):
                df.loc[i, x] = df_stats.loc['50%', x]
print(df)

# 4

def fun(ev):
# В fun будет передан кусок df от groupby под конкретный API. Любая дата 
# будет только по конкретному API, что и использовано в функции
    out = pd.Series()
# Уже есть сортировка по датам, так что можно просто срезать нужный нам 
# промежуток времени, и уже к нему применить сумму
# *Почему-то в LessonPack в предлагаемом ответе взята сумма за 10 первых 
# месяцев, а не за год (12 месяцев). Как будто Prod1Year составлен вот так:
# out['Prod1Year'] = (ev[:10])['Liquid'].sum()
    out['Prod1Year'] = (ev[:12])['Liquid'].sum()
    out['ProdAll'] = ev['Liquid'].sum()
    return out

wells_way = input()
production_way = input()
#wells_way = "data/wells_info.csv"
#production_way = "data/production.csv"
df = pd.read_csv(wells_way)
df2 = pd.read_csv(production_way)
df_group = df2.groupby('API').apply(fun)
# Соединяем 'подяд' по API 
ans = pd.merge(df, df_group, on = 'API')
print(ans)

#
#
#
#
#