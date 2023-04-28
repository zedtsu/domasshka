import random

def zadacha1():
    # Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
    spisok = [random.randint(1, 10) for i in range(int(input('Введите размер списка: ')))]
    print(spisok)
    otvet = lambda x: x > 5
    spisok = list(filter(otvet, spisok))
    print('Результат: ', spisok)


def zadacha2():
    #Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
    spisok = [random.randint(1, 10) for i in range(int(input('Введите размер списка: ')))]
    print('Начальный результат: ', *spisok)
    spisok2 = [(len(spisok))]

    for i in range(len(spisok) // 3):
        spisok2.append(spisok[random.randint(0, len(spisok) - 1)])
    spisok2.sort()
    spisok2 = set(spisok2)
    print('Конечный результат: ', *spisok2)

def zadacha3():
    # Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
    dlina = n = int(input(''))
    spisok = [random.randint(1, 10) for i in range(n)]
    print(spisok)
    spisok = set(spisok)
    print(f'Результат: {spisok}. Удалено повторяющихся элементов: {dlina - len(spisok)}')