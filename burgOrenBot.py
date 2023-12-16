import telebot


API_TOKEN = '6948081472:AAGhv06R-V5Cl4JJdxfEaY5dOnlZiYnwcZ4'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "ПРИВЕТ")
    startKBoard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    webAppTest =  telebot.types.WebAppInfo("https://kirill38105.github.io/burgOren/")  # создаем webappinfo - формат хранения url
    Catalog = telebot.types.KeyboardButton(text="Отзыв", web_app=webAppTest)
    startKBoard.add(Catalog)
    bot.send_message(message.chat.id, "Напишите ваши предложения для улучшения сервиса",reply_markup=startKBoard)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types="web_app_data")  # получаем отправленные данные
def answer(webAppMes):
    print(webAppMes)  # вся информация о сообщении
    print(webAppMes.web_app_data.data)  # конкретно то что мы передали в бота
    bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}")
    # отправляем сообщение в ответ на отправку данных из веб-приложения


bot.infinity_polling()
