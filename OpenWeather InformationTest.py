from pprint import pprint
import requests

apiKey = '52761002532020ab8b2b6f30112eeefa'
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Fort Wayne&APPID='+apiKey)
data = r.json()
pprint(r.json())
tempInKelvin = data['main']['temp']
tempInFarenheit = 1.8 * (tempInKelvin - 273) + 32
pprint(tempInFarenheit)