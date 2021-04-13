import telebot


TELEGRAM_TOKEN = "1786741150:AAF9gKI8UIThbhCqxeGTovSzBtDwteV3V_M"


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])




def send_text(message):
    word = input("Type smth: ")
    vowels = 0
    for i in word:
        letter = i.lower()
        if letter == "a" or letter == "e" or\
        letter == "i" or letter == "o" or\
        letter == "u" or letter == "y":
            vowels += 1
        bot.send_message(message.chat.id, 'Vowels: ' + str(vowels) )
        else:
            pass
        
   
bot.polling()