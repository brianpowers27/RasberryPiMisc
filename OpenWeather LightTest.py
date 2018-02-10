from pprint import pprint
import requests
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import datetime
import time 

#Setup
DesiredTempInFareheit=35
NumSecondsBetweenTries=60
numTimes = 1

##This is the weather stuff
apiKey = '52761002532020ab8b2b6f30112eeefa'


##This is the light stuff
Red = 11
Green = 15 ##pin numbers

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(Red, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(Green, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

##
for i in range(0,numTimes):## Run loop numTimes

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Fort Wayne&APPID='+apiKey)
    data = r.json()    
    tempInKelvin = data['main']['temp']
    tempInFarenheitOutside = 1.8 * (tempInKelvin - 273) + 32
    pprint(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    pprint('Temperature in Fareheit ' +str(int(tempInFarenheitOutside)) )
    pprint('')
    
    #If temp above above sixty light green else red
    if(tempInFarenheitOutside > DesiredTempInFareheit):       
        GPIO.output(Red,False)## Switch on pin 7
        GPIO.output(Green,True)## Switch on pin 7

    else: #temp below desired turn red
        GPIO.output(Red,True)## Switch on pin 7
        GPIO.output(Green,False)## Switch on pin 7

    time.sleep(NumSecondsBetweenTries)## Wait

GPIO.cleanup()
