from email.policy import default
from idlelib.undo import Command


from aiogram import Bot, Dispatcher, types
import asyncio
import requests
from aiogram.filters import Command

bot = Bot(token="7895236981:AAEPPrF-ccAXzpSME-xlg2YlV07eNqKeBVY")
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await  message.answer("Assalamu'alaikum warahmatullah wabarakatuh.😊")

@dp.message()
async def prayer_times(message:types.Message):

    latitude = 41.3895
    longitude = 60.3415
    method = 2  # MWL (Muslim World League)
    timezone = 'Asia/Khiva'


    url = f'http://api.aladhan.com/v1/timings?latitude={latitude}&longitude={longitude}&method={method}&timezone={timezone}'


    response = requests.get(url)


    data = response.json()
    times = (f"🏙 Bomdod : {  data['data']['timings']['Fajr']} \n"
             f"🌅 Quyosh chiqishi :  {data['data']['timings']['Sunrise']} \n"
             f"🏞 Peshin :  {  data['data']['timings']['Dhuhr']} \n"
             f"🌇 Asr : {   data['data']['timings']['Asr']} \n"
             f"🌆 Shom : {  data['data']['timings']['Maghrib']} \n"
             f"🌃 Xufton : {  data['data']['timings']['Isha']} \n"
             f"🌌 Taxajjud : {  data['data']['timings']['Lastthird']}")
    await  message.answer(times)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

