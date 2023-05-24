import random
import telebot

def zadacha1():
    # Задача 1. Создайте пользовательский аналог метода map().
    def sum(a):
        return a + 5

    spisok = [random.randint(0, 10) for i in range(10)]
    print(spisok)
    
    for i in spisok:
        a = map(sum, spisok)
    print(list(a))

    spisok2 = []

    for i in spisok:
        spisok2.append(i + 5)
    print(spisok2)

def zadacha2():
    # Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
    def summa(func):
        def decorator(a):
            print(f'{a} + {a} = ', end=' ')
            func(a)
        return decorator

    @summa
    def sum(a):
        print(a + 1)

    l = input('Введите сколько раз вы хотите вызвать функицю: ')
    l = int(l)

    for i in range(l):
        sum(i)


def zadacha3():
    # Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.
    bot = telebot.TeleBot("6222578607:AAHO37nA3Ezse6VEfNe60grtgTNR0Mgrnik")

    @bot.message_handler(commands=['game'])
    def start(message):
        bot.send_message(message.chat.id, 'Отгдадайте число от 1 до 1000.')

        global number
        number = random.randint(1, 1000)

    @bot.message_handler(content_types=['game'])
    def game(message):
        global number
        attemps = 0
        if message.text.isdigit():
            guess = int(message.text)
            if guess == number:
                bot.send_message(message.chat.id, f'Поздравляю! Вы угадали число за {attempts} попыток.')
            elif guess > number:
                bot.send_message(message.chat.id, 'Загаданное число меньше.')
            elif guess < number:
                bot.send_message(message.chat.id, 'Загаданное число больше.')
            attempts = attemps + 1
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите число от 1 до 1000.')
    bot.polling()