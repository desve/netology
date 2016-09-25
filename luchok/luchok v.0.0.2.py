import config
import telebot
from telebot import types
from tools import save_fs
from tools import read_fs
from tools import get_emotions

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
        downloaded_file = bot.download_file(file_info.file_path)
# Пишем куда грузим
        src='/home/ubuntu/workspace/luchok/'+file_info.file_path;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено") 
    except Exception as e:
        bot.reply_to(message,e )
# Анализ фото
#faceRectangle
    left = get_emotions()['faceRectangle']['left']
    top = get_emotions()['faceRectangle']['top']
    width = get_emotions()['faceRectangle']['width']    
    height = get_emotions()['faceRectangle']['height']    
# scores   
    anger = round(get_emotions()['scores']['anger'], 3)
    contempt = round(get_emotions()['scores']['contempt'], 3)
    disgust = round(get_emotions()['scores']['disgust'], 3)
    fear = round(get_emotions()['scores']['fear'], 3)
    happiness = round(get_emotions()['scores']['happiness'], 3)
    neutral = round(get_emotions()['scores']['neutral'], 3)
    sadness = round(get_emotions()['scores']['sadness'], 3)
    surprise = round(get_emotions()['scores']['surprise'], 3)
# Вывод данных
    hi = "И вот, что я о тебе расскажу:"
    bot.send_message(message.chat.id, hi)    
    hi = "Гнев/Anger-" + str(anger)
    bot.send_message(message.chat.id, hi)     
    hi = "Презрение/Contempt-" + str(contempt)
    bot.send_message(message.chat.id, hi) 
    hi = "Отвращение/Disgust-" + str(disgust)
    bot.send_message(message.chat.id, hi)  
    hi = "Страх/Fear-" + str(fear)
    bot.send_message(message.chat.id, hi)     
    hi = "Счастье/Happiness-" + str(happiness)
    bot.send_message(message.chat.id, hi)    
    hi = "Нейтральность/Neutral-" + str(neutral)
    bot.send_message(message.chat.id, hi)           
    hi = "Печаль/Sadness-" + str(sadness)
    bot.send_message(message.chat.id, hi)        
    hi = "Сюрприз/Surprise-" + str(surprise)
    bot.send_message(message.chat.id, hi)   
     
     
# Handles all text messages that contains the command '/help'.
@bot.message_handler(commands=['help'])
def handle_help(message):
    pass

if __name__ == '__main__':
     bot.polling(none_stop=True)