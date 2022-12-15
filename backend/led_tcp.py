import socket
from time import sleep

HOST = "10.0.0.252"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

def read_data(filename):
    dat = ""
    with open(filename, 'r') as dataf:
        dat += dataf.read()
        dataf.close()
    return bytearray.fromhex(dat)

def transmit_data(data, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
        s.close()

def run_repeatedly():
    while(True):
        data = read_data("data")
        print("read " + str(len(data)) + " bytes")
        transmit_data(data, HOST, PORT) #TODO allow multiple devices
        sleep(0.05)

#run_repeatedly()

data = read_data("data")
transmit_data(data, HOST, PORT)
