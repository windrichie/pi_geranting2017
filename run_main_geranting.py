##///**
##//* Solar Panel Output Voltage Reading - RasPi Side
##//* Pulau Geranting
##//*
##//* @description
##//* receive voltage reading from arduino
##//* relay to data.sparkfun.com/solar_geranting
##//*
##//* Author: Edward
##//* Alva Energi
##//* last edited: 21/2/2017
##//**/

import httplib, urllib
import socket
import time
import serial
import sys
import logging
from serial.tools import list_ports

### server config
server = "data.sparkfun.com" # base URL of your feed
publicKey = "DJ4Mgggn7KSpojdygvVp" # public key, everyone can see this
privateKey = "P4rokkk6WzUgzYpX9AGg"  # private key, only you should know
fields = ["volt", "amps"] # Your feed's data fields

### output log
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('/home/pi/Desktop/geranting/logs/main_log.txt')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

# other variables
arduino_on = True

def send2DataSpark(data):
        logger.info("sending data to dataspark server")

        # encode to url
        params = urllib.urlencode(data)

        # setup headers
        headers={}
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Connection"] = "close"
        headers["Content-Length"] = len(params) # length of data
        headers["Phant-Private-Key"] = privateKey # private key header

        try:
            # Now we initiate a connection, and post the data
            c = httplib.HTTPConnection(server)

            # Here's the magic, our request format is POST, we want
            # to send the data to data.sparkfun.com/input/PUBLIC_KEY.txt
            # and include both our data (params) and headers
            c.request("POST", "/input/" + publicKey + ".txt", params, headers)
            r = c.getresponse() # Get the server's response and print it
            logger.info("%s, %s", r.status, r.reason)
        except httplib.BadStatusLine:
            logger.warning("unknown server response")
        except socket.gaierror:
            logger.error("not connected to internet")
    

if __name__ == "__main__":
        logger.info('bootup') 
        
        while True:
                
                # read data from arduino
                try:
                    # serial configuration -> udev mapped arduino_uno to ttyACM*
                    ser = serial.Serial('/dev/arduino_uno', 115200, timeout=2)
                    data_raw = ser.readline()
                    # arduino is connected
                    arduino_on = True
                # if arduino is not connected
                except serial.SerialException:
                    # activate this once when arduino is not connected
                    if(arduino_on):                            
                            arduino_on = False
                            data_raw = "arduino not connected, arduino not connected"
                            logger.error("arduino is not connected")
                    
                # if there's data, send to web server
                if(data_raw.__len__() > 0):

                    try:
                            # split string into Volt and Amp
                            voltAmp = data_raw.split(",")

                            data = {}
                            data[fields[0]] = voltAmp[0].strip()
                            data[fields[1]] = voltAmp[1].strip()
                    except IndexError:
                            data[fields[0]] = "missing data"
                            data[fields[1]] = "missing data"                                
                            
                    # send data to web server
                    send2DataSpark(data)

                    #reset data_raw
                    data_raw = ""

                ##time.sleep(1)

