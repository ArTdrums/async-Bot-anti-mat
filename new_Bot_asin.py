from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ContentType, Message, InputFile
from slovar_polit_slov import slov_polit_slov_chek
from токены.token_asinBot import token
from slosar_mat_slov import *

text_mat = ''
text_polit = ''

bot = Bot(token=token)  # создаем бота на базе класса бот
dp = Dispatcher(bot)  # обрабатывает все обновления бота


@dp.message_handler(commands=['start'])
async def com_ctr(message: types.Message):
    await message.answer('привет, я бот')


@dp.message_handler(commands=['help'])
async def help_com(message: types.Message):  # передаем сообщение на базе класса мессадж
    await message.reply('этот бот следит за корректностью вашего текста')


# хендлер для поучения id фото от бота, нужно скинуть картинку боту и он пришлее его id в чат
@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):  # импорт Message делаешь через правую кнопку из aiogram MessageType
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(text='/video')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    photo_puti = InputFile(path_or_bytesio='../media/pik.png')
    # можно добавить фото двумя способами
    # photo_id -это id, который присылает бот после отработки хендлера id
    # photo_puti

    # await dp.bot.send_photo(chat_id=chat_id, photo=photo_puti)
    await dp.bot.send_video(chat_id=chat_id,
                            video='BAACAgIAAxkBAAMWYyRl0I3HK9LkZlT6YZqH4T1wjwkAAmQdAALg2CBJ5cmvSoYxiw8pBA')


@dp.message_handler(content_types=['text'])
async def text_chek(message: types.Message):  # передаем сообщение на базе класса мессадж
    text_mat = message.text.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(
        '/n', ' ')

    text_polit = message.text.lower()
    a = text_polit.split()
    b = text_mat.split()

    for i in range(len(a)):
        if a[i] in slov_polit_slov_chek.values():
            a = 'тут не место политике'
            await message.answer(a)

    for i in range(len(a)):

        if b[i] in slovar_itog.values():
            b[i] = '***'

    n = (' '.join(b))
    await message.answer(n)


executor.start_polling(dp)
