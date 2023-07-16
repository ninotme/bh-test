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
        
        print('DEBUG PACKET INFO: ', bData) 
        
        conn.sendall(bData)
        

if __name__ == '__main__': 
    HOST  = 'localhost'
    PORT = 9997
    
    print('OPENING SOCKET') 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect( (HOST, PORT))
    print('CONNESSIONE STABILITA')
    #try sending a non-json message
    data = b'WORLD'
    
    
    __send_data_to_client(s, SMessage.hellom(),  data)  
    print('Dopo chiamata __send_data, aspetto s.recv()')
    data = s.recv(1024) 
    
    print("received data...", data) 
    
    #close connection 
    print("invio close request, parametri")
    
    
    __send_data_to_client(s, SMessage.stopm(), 'Connection ended gracefully') 
    
    print("close request inviata. termino il client") 
    
