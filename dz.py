import numpy as np
import random

def zadacha1():
    # Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

    dlina = int(input('Введите размер списка: '))
    spisok = np.random.randint(0, 10, dlina)
    print(spisok)

    spisok2= np.unique(spisok)

    print(f'Количесвто уникальных элементов: {len(spisok2)}.')

def zadacha2():
    # Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

    a = [1, 1, 1, 1, 1]
    b = [2, 3, 4, 2, 4]
    c = [4, 6, 2, 4, 5]
    d = [1, 1, 1, 1, 1]
    e = [1, 1, 1, 1, 0]

    matrix = [a, b, c, d, e]
    matrix = np.array(matrix)
                
    print(matrix)

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)): 
            if np.array_equal(matrix[i], matrix[j]):
                if np.array_equal(matrix[:, i], matrix[:, j]):
                    print(i, j)

               
def zadacha3():
    # Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
    # Выведите элементы главной диагонали матрицы в виде одномерного массива.

    a, b = random.randint(4, 10), random.randint(4, 10)

    matrix = np.random.randint(0, 10, (a, b))

    print(matrix)

    print(f'Мин: {np.min(matrix)}. Макс: {np.max(matrix)}')

    print(f'Главная диагональ: {np.diag(matrix)}')

zadacha2()