from serial import Serial
from time import sleep
def arduino(key,val):

    ser = Serial('/dev/ttyUSB0')
    c1 = 0.005  #right
    c2 = 0.005  #left

    if key == 'r':
        if val>0:
            ser.write(b'r')
            sleep(c1*val)
        else
            val=-val
            ser.write(b'l')
            sleep(c1*val)
    elif key == 'f':
        ser.write(b'f')
        sleep(val)
    elif key == 's':
        ser.write(b's')
        sleep(val)

    sleep(0.5)
    
