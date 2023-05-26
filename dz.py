import telebot

def zadacha1():
	# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
	bot = telebot.TeleBot("")

	@bot.message_handler(commands=['start'])
	def welcome(message):
		bot.reply_to(message, "Здравствуйте, если вы хотите добавить что-нибудь в тех. поддержку напиишите комманду: /TP")

	@bot.message_handler(commands=['tp'])
	def TP(message):
		bot.reply_to(message, "Вы обратились в тех. поддержку, наишите ваше обращение:")

	@bot.message_handler(content_types=['text'])
	def otvet(message):
		text = message.text
		data = open('TP.txt', mode='a', encoding='utf-8')
		data.write(text)
		data.close()
		bot.reply_to(message, 'Спасибо, мы очень ценим ваше мнение!')

	bot.polling()

def zadacha2():
	# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.
	data= open('text.txt', mode='a', encoding='utf-8')
	text = input('Введите свой вопрос, мы обработаем его и ответим: ')
	data.write(f'{text}\n')
	data.close()

	data = open('text.txt', mode='r', encoding='utf-8')
	print(f'Вопрос: {data.readline()}.')
	print(f'Ответ: я не знаю :D.')
	data.close()