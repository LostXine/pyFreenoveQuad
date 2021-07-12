import serial
import socket
import Orders
import time

class TcpConnection:
    def __init__(self, addr='192.168.4.1', port=65535):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.host = addr
        self.port = port
        self.is_open = False
        
    def open(self):
        self.sock.settimeout(5)
        try:
            self.sock.connect((self.host, self.port))
            self.is_open = True
            self.sock.settimeout(0.5)
        except:
            traceback.print_exc()
            print('TCP connection failed.')
            self.sock.close()
            return

    def close(self):
        if self.is_open:
            self.sock.close()
            self.is_open = False
            
    def write(self, data):
        if self.is_open:
            try:
                self.sock.send(data)
                return True
            except socket.timeout:
                print("Connection timeout, closed")
                self.close()
                return False
        else:
            print("Connection failed")
            return False
            
    def read_until(self, expected):
        if self.is_open:
            try:
                data = self.sock.recv(16)
            except socket.timeout:
                data = b''
            return data
        else:
            print("Connection failed")
            return b''


class Communication:
    
    def __init__(self, client):
        self.client = client

    def open(self):
        if not self.client.is_open:
            self.client.open()
        
    def is_open(self):
        return self.client.is_open
        
    def close(self):
        if self.client.is_open:
            self.client.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()
    
    def __write(self, data):
        if self.client.is_open:
            dataWrite = bytes([Orders.transStart] + data + [Orders.transEnd])
            print('Write: ', dataWrite)
            ret = self.client.write(dataWrite)
            if ret is None:
                return True
            else:
                return ret
                
        else:
            print("Client is not available")
            return False
    
    def __read(self):
        if self.client.is_open:
            dataRead = b''
            
            while len(dataRead) == 0:
                try:
                    dataRead = self.client.read_until(expected=bytes([Orders.transEnd]))
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    print("Interrupt read")
                    return b''
            else:
                print("Read: ", dataRead)
                return dataRead[1:-1]
        else:
            print("Client is not available")
            return b''
    
    def send_command(self, outData):
        if self.__write(outData):
            print("Cmd sent, wait for response")
            inData = self.__read()
            
            if inData != b'':
                if inData[0] == Orders.orderStart:
                    self.wait_command_done()
            return inData
        else:
            return None

    def wait_command_done(self):
        inData = self.__read()
        if inData != b'':
            if inData[0] == Orders.orderDone:
                return True
        return False

