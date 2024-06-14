# Основа класса Item с лекции
# Для удобства изначальное количество предметов - 0, максимум - 20
class Item:
    def __init__(self, count = 0, max_count = 20):
        self.count = count
        self.max_count = max_count
        
    def update_count(self, val):
        if val <= self.max_count:
            self.count = val
            return True
        else:
            return False
    #1 (Уже реализовано в лекции)
    def __add__(self, num):
        return self.count + num
    
    def __mul__(self, num):
        return self.count * num
    
    def __lt__(self, num):
        return self.count < num
    
    def __len__(self):
        return self.count
    #2 
    #(Написано по аналогии)
    def __sub__(self, num):
        return self.count - num
    
    def __gt__(self ,num):
        return self.count > num
    
    def __lt_or_eq__(self, num):
        return self.count <= num
    
    def __gt_or_eq__(self, num):
        return self.count >= num
    
    def __eq__(self, num):
        return self.count == num
    # Принцип для -=, +=, *= один и тот же - если результат лежит в пределах
    # [0, max_count], то обновление допускается, иначе поднимается ошибка
    def __isub__(self, num):
        local_count = self.count - num
        if ((local_count >= 0) and (local_count <= self._max_count)):
            self.count = local_count
        else:
            raise IndexError("Resulting value out of range!")
            
    def __isum__(self, num):
        local_count = self.count + num
        if ((local_count >= 0) and (local_count <= self._max_count)):
            self.count = local_count
        else:
            raise IndexError("Resulting value out of range!")
            
    def __imul__(self, num):
        local_count = self.count * num
        if ((local_count >= 0) and (local_count <= self._max_count)):
            self.count = local_count
        else:
            raise IndexError("Resulting value out of range!")
    def __del__(self):
        pass
#3
# Реализации Fruit и Food так же взяты с лекции
class Fruit(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self.ripe = ripe


class Food(Item):
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self.saturation = saturation
    @property
    def eatable(self):
        return self.saturation > 0

# Съедобный (потенциально) фрукт 1
class Banana(Fruit, Food):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self._color = color
    @property
    def color(self):
        return self._color    
    @property
    def eatable(self):
        return super().eatable and self.ripe

# Съедобный (потенциально) фрукт 2
class Pineapple(Fruit, Food):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self._color = color
    @property
    def color(self):
        return self._color    
    @property
    def eatable(self):
        return super().eatable and self.ripe

# Съедобный (потенциально) не-фрукт 1
class Bread(Food):
    def __init__(self, moldy = False, **kwargs):
        super().__init__(**kwargs)
        self.moldy = moldy

    def eatable(self):
        return super().eatable and not(self.moldy)

# Съедобный (потенциально) не-фрукт 2        
class Pelmeni(Food):
    def __init__(self, boiled = False, frozen = True, **kwargs):
        super().__init__(**kwargs)
        self.boiled = boiled
        self.frozen = frozen
    
    def eatable(self):
        return self.boiled and not(self.frozen) and super().eatable
    
    def vkusno(self):
        if self.eatable:
            print ('YES')
        else:
            print('no :(')
#4
# Пусть всего в списке Inventory будет 20 элементов
class Inventory:
    def __init__(self):
        self.lst = [None for _ in range(0,20)]
# Чтобы добавлять съедобные элементы, заведём функцию madd (...: int
# синтаксический сахар - теперь, если попытаться передать inv.madd(banan, 6), 
# компилятор поймёт какой элемент какой переменной соответствует)
# Если переданный объект (по условию - еда) не является съедобным, поднимаем
# ошибку. Если количество объекта уже равно нулю, ничего не происходит
    def madd(self, mindex: int, mfood):
        if (mfood.count == 0):
            pass
        elif(mfood.eatable()):
            self.lst[mindex] = mfood
        else:
            raise "Given food isn't eatable"
# Для работы с количеством была определена функция update_count, определённая 
# для всех объектов класса Item, а следовательно унаследованная классами, 
# содержащими в себе eatable. Если update_count вернул False, будем поднимать 
# ошибку. Если update_count вернул True, необходимо выполнить проверку - если
# количество стало нулевым, нужно удалить объект из списка. Если пользователь
# пытается вызвать изменение количества в пустой ячейки, поднимается ошибка.
    def change_amount(self, mindex, new_amount):
        if (self.lst[mindex] != None):
            if (self.lst[mindex].update_count(new_amount)):
                if (self.lst[mindex].count == 0):
                    self.lst[mindex] = None
            else:
                raise "Given amount is greater then maximum"
        else:
            raise "This cell is empty"
#5
# Создадим класс с изначально недоступным пустым списком. Менять список 
# пользователь сможет с помощью комманд qPush и qPop, очевидно первая добовляет
# элемент в конец списка , вторая - удаляет первый элемент из списка 
class mQueue:
    def __init__(self):
        self._lst = []
    
    def qPush(self, elem):
        self._lst.append(elem)
# list.pop, помимо удаления элемента, двигает остаток массива 
    def qPop(self):
        self._lst.pop(0)
    
# Чтобы была возможность получить полную очередь, реализуем функцию getQ,
# при этом создавая полноценную копию списка, созданного очередью (грубо говоря
# если написать return _lst будет создан указатель на тот же список)
    def getQ(self):
        lst_mim = []
        for i in self._lst:
            lst_mim.append(i)
        return lst_mim
#
#
#
#
#