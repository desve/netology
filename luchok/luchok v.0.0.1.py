import config
import telebot
from telebot import types
from tools import save_fs
from tools import read_fs

bot = telebot.TeleBot(config.token)


# Handles all text messages that contains the command '/start'.
@bot.message_handler(commands=["start"])
def send_welcome(message):
#    markup = types.ReplyKeyboardHide()
#    video = open('cards/start.gif', 'rb')
#    tb.send_video(message.chat.id, video)
    hi1 = ("Hi! I am Luchok! v.0.0.1")
    hi2 = " А как тебя зовут?"
    hi = hi1 + hi2
# sendMessage
    bot.send_message(message.chat.id, hi)
    fs = 10                             
    save_fs(fs)

@bot.message_handler(content_types=["text"])
def tell_messages(message):
    final_state = int(read_fs())
# sendMessage
    hi = "Привет, " + message.text + "!"
    bot.send_message(message.chat.id, hi)
# sendMessage
    hi = "Загрузи свое фото и я расскажу о тебе все:=)"
    bot.send_message(message.chat.id, hi)  
   
    
# Handles all sent photo files
@bot.message_handler(content_types=['photo'])
def handle_photo(message):  
    try: 
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        print("Мы тут 2")
        print('file_info=', file_info)
        print('len(message.photo)=', len(message.photo))
#        print('file_id=', file_id)
        print('file_path=', file_info.file_path)
        downloaded_file = bot.download_file(file_info.file_path)
        print("Мы тут 3")
# Пишем куда грузим
        src='/home/ubuntu/workspace/luchok/'+file_info.file_path;
        print("Мы тут 4")
        print('src=', src)
        with open(src, 'wb') as new_file:
            print("Мы тут 5")
            new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено") 
        print("Мы тут 6")
   
    except Exception as e:
        print("Мы тут 7")
        bot.reply_to(message,e )

     
# Handles all text messages that contains the command '/help'.
@bot.message_handler(commands=['help'])
def handle_help(message):
    pass

if __name__ == '__main__':
     bot.polling(none_stop=True)