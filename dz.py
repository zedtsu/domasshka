def zadacha1():
    # Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
    n = int(input('Введите число: '))
    fac = 1
    
    print('Результат: ', end='')
    for j in range(1, n):
            fac *= j
            print(fac, end=', ')
    print(fac * n)

def zadacha2():
    # Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                print(f'{x} {y} {z}')

def zadacha3():
    # Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
    n = str(input('Введите первую строку: '))
    o = str(input('Введите вторую строку: '))

    print('Результат: ', end='')
    for i in range(len(n)):
        count_aa = 0
        for j in range(len(o)):
            if o[j] == n[i]:
                count_aa += 1
        print(f'{n[i]} = {count_aa} ', end='')

def zadacha4():
    # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
    N = 10
    lst = list(range(-N, N+1))
    shift = 2
    lst = lst[-shift:] + lst[:-shift]
    print(lst)