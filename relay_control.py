import RPi.GPIO as GPIO
import datetime
#import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.OUT)

while (True):
    timenow=datetime.datetime.now()
    if (18<=timenow.hour<=23):
        if (timenow.hour==18):
            if (timenow.minute>45):
                GPIO.output(37,GPIO.HIGH) #night time, turnon LED
            else:
                GPIO.output(37,GPIO.LOW) #day time, turnoff LED
        else: 
            GPIO.output(37,GPIO.HIGH) #night time, turnon LED
    else:
        GPIO.output(37,GPIO.LOW) #daytime, turnoff LED