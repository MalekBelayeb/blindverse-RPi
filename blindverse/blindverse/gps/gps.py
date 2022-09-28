import serial
import pynmea2
import sys
from Adafruit_IO import Client
sys.path.append('/home/blindverse/Desktop/blindverse-RPi/blindverse/blindverse/utils/consts')

def execute_send_gps():
    ADAFRUIT_IO_KEY = 'aio_tzaF313Fb7FXmbOTQDqVoedW0fHS'
    ADAFRUIT_IO_USERNAME = 'blindverse'
    aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

    while True:
        port = "/dev/serial0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()
        test = bytes("$GPRMC", 'utf-8')
        if newdata[0:6] == test:
            newmsg = pynmea2.parse(newdata.decode())
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
            gpsmqtt = str(lat) + "," + str(lng) + ",62fb635db4ac1a3fb7270f67"
            print(gps)
            aio.send('gps', gpsmqtt)
            break
        
        
        
execute_send_gps()    
