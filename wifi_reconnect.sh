#!/bin/bash

# reference: alexba.in/blog/2015/01/14/automatically-reconnecting-wifi-on-a-raspberrypi/

# Try Ping Google Server
SERVER=8.8.8.8

# send two pings
ping -c2 ${SERVER} > /dev/null

# if the return code from ping ($?) is not 0 (meaning there was an error)
if [ $? != 0 ]; then
	# restart the wireless interface
	ifdown --force wlan0
	ifup wlan0
fi