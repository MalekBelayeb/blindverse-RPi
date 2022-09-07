import sys
sys.path.append('/home/blindverse/Desktop/blindverse-RPi/blindverse/')

from socket_connector import connect_socket
from mode_selector import mode_selector

def main():
    
    socket = connect_socket()
    result = mode_selector(socket)
    print(result)
    
if __name__ == '__main__':
    main()