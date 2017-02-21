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
##//* last edited: 18/2/2017
##//**/

import httplib, urllib
import socket
import time
import serial
import sys
import logging

### server config
server = "data.sparkfun.com" # base URL of your feed
publicKey = "DJ4Mgggn7KSpojdygvVp" # public key, everyone can see this
privateKey = "P4rokkk6WzUgzYpX9AGg"  # private key, only you should know
fields = ["volt"] # Your feed's data fields

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
    

if __name__ == "__main__":
    logger.info('bootup')
    
    while 1:
        # read data from arduino
        try:
            # serial configuration
            ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)
            data_raw = ser.readline()
        # if arduino is not connected
        except serial.SerialException:
            data_raw = "arduino not connected"
            logger.error("arduino is not connected")
            
        # if there's data, send to web server
        if(data_raw.__len__() > 0):
            data = {}
            data[fields[0]] = data_raw

            send2DataSpark(data)
            
        
        ##time.sleep(1)

