import RPi.GPIO as GPIO
import datetime
import time
import os
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
LED_ON = False

def post_firebase():
    if (LED_ON==True):
        data = {'timestamp':datetime.datetime.now(),'status':'LED ON'}
        result = firebase.post('/LED_status',data)
    else: 
        data = {'timestamp':datetime.datetime.now(),'status':'LED OFF'}
        result = firebase.post('/LED_status',data)

if __name__ == '__main__':
    
    SECRET = os.environ("FIREBASE.SECRET")
    DSN = 'https://jakartasmartpark.firebaseio.com/'
    EMAIL = 'tamanhijaujakarta'
    authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
    firebase = FirebaseApplication(DSN, authentication)

    while 1:
        timenow=datetime.datetime.now()
        if (18<=timenow.hour<=23):
            if (timenow.hour==18):
                if (timenow.minute>=45):
                    if (LED_ON == False):
                        GPIO.output(37,GPIO.HIGH) #night time, turnon LED
                        LED_ON = True
                        post_firebase()
            else:
                if (LED_ON == False):
                    GPIO.output(37,GPIO.HIGH) #night time, turnon LED
                    LED_ON = True
                    post_firebase()
        else:
            if (LED_ON==True):
                GPIO.output(37,GPIO.LOW) #daytime, turnoff LED
                LED_ON = False
                post_firebase()
            
        time.sleep(60)