import telebot

access_token = '1184780361:AAHFnxVUIX3hkZ2o52dGfCJozenvYM2tdyQ'
telegram.apihelper.proxy = {'https': 'https://23.237.22.172:3128'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)

# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()
    