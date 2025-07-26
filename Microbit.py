import serial

import time

ser = serial.Serial()

ser.baudrate = 115200

ser.port = "COM5"

ser.open()

while True:
    
    data = str(ser.readline())
    
    data = data.replace("b","")
    
    data = data.replace(" ","")
    
    data = data.replace("\\n","")
    
    data = data.replace("\\r","")
    
    print(data)
    
    time.sleep(1)
    
    