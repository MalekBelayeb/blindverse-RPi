import socket

def connect_socket():
    s = socket.socket()
    s.bind(('0.0.0.0', 8091))
    s.listen(0)
    return s