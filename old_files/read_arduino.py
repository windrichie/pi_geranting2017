import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)

while 1:
    data = ser.readline()

    if(data.__len__() > 0):
        print(ser.readline())
