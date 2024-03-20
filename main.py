import telebot
import requests
import json
bot = telebot.TeleBot('7105655965:AAHt8i4oVlqQ8z2FHaBXbagG2yveEYp7E-k')
API = '3d9de74844d28377e81415151cbe6a66'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    bot.reply_to(message, f'Сейчас погода: {temp}')
    image = 'jara.jpg' if temp > 5.0 else 'holod.jpg'
    file = open('./' + image, 'rb')
    bot.send_photo(message.chat.id,file)

bot.polling(non_stop=True)