# Режимы открытия файлов. Задача "Учёт товаров"

#from pprint import pprint  # функция «pprint» позволяет нам делать вывод в терминал более удобно читаемым


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    # def __init__(self, name, weight, category):
    #     super().__init__(name, weight, category)

    def get_products(self):
        file = open(self.__file_name, 'r')
        #str_f = pprint(file.read())
        str_f = file.read()
        file.close()
        return f'{str_f}'

    def add(self, *products):
        #file = open(self.__file_name, 'r')
        str_f1 = self.get_products().splitlines()  # возвращает список строк, текста str_f, разделенного по
        # универсальным разрывам строк
        l_prod = [line.split(',')[0].strip() for line in str_f1] # создадим список имен уже существующих
        # продуктов по наименованиям. Проходим по каждой строке (for line in str_f1), делим элементы каждой строки
        # запятыми (',') и берем первый-наименование. удаляем начальные и конечные пробелы из строки strip()
        for i in products:
            if i.name in l_prod:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{str(i)}\n')
                file.close()
                l_prod.append(i.name) # добавляем имя нового продукта в лист существующих продуктов


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
