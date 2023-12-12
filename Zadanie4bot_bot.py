from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token="6499428662:AAHvtaekrMMnDHR37CcIWZsBXdpQ4AFq-EE")
dp = Dispatcher(bot)
try:
    with open ("zadaniya/zadanie4/sp_gr.txt", "r", encoding="utf-8") as file1:
        students = [line1.strip("\n")for line1 in file1]
        students =list(filter(None, students))
except FileNotFoundError:
    print(f"Файл 'sp_gr.txt' не найден")
        

with open ("zadaniya/zadanie4/zadaniya.txt", "r", encoding="utf-8") as file2:
    zadaniya = [line2.strip("\n")for line2 in file2]
    zadaniya =list(filter(None, zadaniya))    

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    buttons = [
        [types.KeyboardButton(text="Help")],
        [types.KeyboardButton(text="Что-то")]
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons,  resize_keyboard=True)

    await message.answer(text="🏆Привет, <em>введи свою фамилию:</em>", parse_mode="HTML", reply_markup=keyboard)

HELP_COMMAND = """Этот бот поможет тебе подобрать студента для тайного санты
/help - список команд💥
/start - начать работу💥"""
@dp.message_handler(lambda message: message.text == "Help")
async def help1_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()
    
@dp.message_handler(commands=["help"])
async def help2_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")

@dp.message_handler()
async def zadaniya_command(message: types.Message):
    found = False
    
    a=random.choice(zadaniya)
    for name in students:
        if name.startswith(message.text):
            found=True
            break
    if found == True:
        await message.answer(text=f"Студент которому вы теперь должны подарок это.... {a}")
    else:
        await message.answer(text="Такого студента нет")
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
