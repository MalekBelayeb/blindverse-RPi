import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')
import serial
import pynmea2
import socket
from blindverse.utils.consts import SOCKET_SERVER_HOST, SOCKET_SERVER_PORT

def execute_send_gps():
    client_socket = socket.socket()
    client_socket.connect((SOCKET_SERVER_HOST,SOCKET_SERVER_PORT))
    message = 'GPS_ALERT'
    client_socket.send(message.encode())
    client_socket.close()
    return 'GPS alert sent to trust'

#execute_send_gps()
