import serial
import time
powerOff = "\xAA\x11\xFE\x01\x00\xBA"
ser = serial.Serial(
                    port='COM1',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)  # open serial port

time.sleep(1)            #para que le de tiempo a abrir
#print(ser.name)         # check which port was really used
ser.write(powerOff)
ser.close()              # close port