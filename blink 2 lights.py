import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

led1 = 11
led2 = 15 ##pin numbers

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(led1, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(led2, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

##Define a function named Blink()
def Blink(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
        print "Iteration " + str(i+1)## Print current loop
        GPIO.output(led1,True)## Switch on pin 7
        GPIO.output(led2,False)## Switch on pin 7
        time.sleep(speed)## Wait
        GPIO.output(led1,False)## Switch off pin 7
        GPIO.output(led2,True)## Switch off pin 7
        time.sleep(speed)## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))
