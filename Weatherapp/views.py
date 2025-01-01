from django.shortcuts import render, HttpResponse
import requests
import datetime

def index(request):
    # print(request.POST)
    if 'city' in request.POST:
        city = request.POST['city']
    else :
        city = "indore"
    print(city)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=eccc283ab028bf19b1ed920daedf25ae"
    PARMS = {'units':'metric'}

    data = requests.get(url,PARMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    # rain = data['rain']['1h']

    day = datetime.date.today()

    return render(request,'index.html',{"description":description,"icon":icon,"temp":temp,"day":day,'city':city,"humidity":humidity,"wind":wind})