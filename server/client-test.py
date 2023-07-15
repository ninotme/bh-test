# test client for controller interaction 

import socket 
from messages import SMessage
import json

def __send_data_to_client(conn, typem, data):
        write_data_msg = {
            "type": typem,
            "data": data
             }
        data = json.dumps(write_data_msg)
        bData = bytes(data)
        conn.sendall(bData)

if __name__ == '__main__': 
    HOST  = 'localhost'
    PORT = 9997
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect( (HOST, PORT))
    
    #try sending a non-json message
    data = 'hello'
    
    
    __send_data_to_client(s, SMessage.hellom(),  data)  
    
    data = s.recv(1024) 
    
    print('received data') 
    
    #close connection 
    __send_data_to_client(s, SMessage.stopm(), 'Connection ended gracefully') 
    
