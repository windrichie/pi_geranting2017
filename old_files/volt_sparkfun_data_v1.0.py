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

### NOTES: THIS IS IMPROPER, USE PYTHON'S LOGGING METHOD
log = open('volt_log.txt', 'a')
old_stdout = sys.stdout
sys.stdout = log

def send2DataSpark(data):
        print("send2server")

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

            # Here's the magic, our reqeust format is POST, we want
            # to send the data to data.sparkfun.com/input/PUBLIC_KEY.txt
            # and include both our data (params) and headers
            c.request("POST", "/input/" + publicKey + ".txt", params, headers)
            r = c.getresponse() # Get the server's response and print it
            print r.status, r.reason
        except httplib.BadStatusLine:
            print("unknown server response")
    

if __name__ == "__main__":
    print('boot-up')

    while 1:
        # read data from arduino
        try:
            # serial configuration
            ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)
            data_raw = ser.readline()
        # if arduino is not connected
        except serial.SerialException:
            data_raw = "arduino not connected"
            print("arduino not connected")
            
        # if there's data, send to web server
        if(data_raw.__len__() > 0):
            data = {}
            data[fields[0]] = data_raw

            send2DataSpark(data)
            
        
        ##time.sleep(1)

