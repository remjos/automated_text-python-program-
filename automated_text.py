import schedule
import time
from phone_number import phone_number
import json, requests
#must use a valid API key here
from weather_api_key import weather_api_key
from text_api_key import text_api_key


weather_api_key = weather_api_key
city = "Houston"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+weather_api_key+"&units=imperial"


request = requests.get(url)
json = request.json()

#variable declartion for the if statements
temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")
humidity = json.get("main").get("humidity")

wind_speed = json.get("wind").get("speed")


# class Text_message:
#     def __init__(self, temperature, humidity, phone_number):
#         self.__init__
#         self.temperature = temperature
#         self.humidity = humidity
#         self.phone_number = phone_number

# t1 = Text_message(temp_max, humidity)
# phone = Text_message(phone_number)

def send_good_weather_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'the weather is perfect, go take a walk',
        'key': text_api_key,
})
    print(resp.json())

def send_bad_weather_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'the weather is not good, do not go outside',
        'key': text_api_key,
    })
    print(resp.json())

if temp_max > 65 < 75 and humidity < 70:
    send_good_weather_message()
else:
    send_bad_weather_message()
    
    
    

def send_message_monday():

    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Good evening, please vacuum the entire house and conduct the daily evening cleaning tasks',
        'key': 'textbelt',
    })
    print(resp.json())

def send_message_tuesday():

    resp = request.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Clean all the bathrooms, master, guest and spare upstairs',
        'key': 'textbelt',
    })
    print(resp.json())

def send_message_wednesday():

    resp = request.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Dust everything - fans, mantel, tvs, etc.',
        'key': 'textbelt',
    })
    print(resp.json())

def send_message_thursday():

    resp = request.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Mop all floors including bathroom areas',
        'key': 'textbelt',
    })
    print(resp.json())

def send_message_friday():

    resp = request.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Monthly chore, 1st = Wipe basboards and cabinets, 2nd = Clean stove and microwave, 3rd = Clean out fridge and freezer (garage and indoor) 4th = Clean windows inside and out',
        'key': 'textbelt',
    })
    print(resp.json())

def send_message_saturday():

    resp = request.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Conduct the laundry for the week and complete any project you have been wanting to get done',
        'key': 'textbelt',
    })
    print(resp.json())


    if temp_max > 80:
        print("it's way too hot, stay inside")
    elif humidity > 65:
        print("Do not go outside, it's so humid it's bascailly raining lol")
    elif temp_max < 78:
        print("it's actually pretty nice out")


    schedule.every().monday.at("19:00").do(send_message_monday())

    schedule.every().tuesday.at("19:00").do(send_message_tuesday())

    schedule.every().wednesday.at("19:00").do(send_message_wednesday())

    schedule.every().thursday.at("19:00").do(send_message_thursday())

    schedule.every().friday.at("19:00").do(send_message_friday())

    schedule.every().monday.at("16:48").do(send_message_saturday())

    #schedule.every().monday.at("16:13").do(send_message_sunday())

while True:
    schedule.run_pending()
    time.sleep(0)
