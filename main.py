import types
from aiogram import *
from config import *
from pytube import YouTube
import os



bot = Bot(token)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Привет! давай скачаем видосик с Youtube, отправь мне ссылку: ')
  

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://youtu.com/':
        await bot.send_message(chat_id, f'<b>Начинаем загрузку: {yt.title}</b>', parse_mode= 'html')
        await download_youtube(url, message, bot)

async def download_youtube(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive = True, file_extension = "mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption= 'Вот твой видосик')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')

if __name__ == '__main__':
    executor.start_polling(dp)

# bot.polling(non_stop=True)
