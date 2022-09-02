from socket_connector import connect_socket
from mode_selector import mode_selector

def main():

    socket = connect_socket()
    mode_selector(socket)

if __name__ == '__main__':
    main()


