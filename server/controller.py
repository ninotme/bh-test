from messages import SMessage 
import json 
import socket



class Service:
    
    def ectrl_connected(self): 
        print('connesso') 
        
        
    def ectrl_disconnected(self): 
        print('disconesso')
        self.conn.close() 
        
    def ectrl_hello(self, data): 
        print('hello function')
        print('Elaborating...') 
        print(f'hello {data}') 

        
    def ectrl_close(self,info): 
        print('closing connection...') 
        print(f"info: {info}") 
        self.conn.close()
        
    def host(self, host, port):  
        HOST = host               
        PORT = port             
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("connecting socket")
        self.socket.bind((HOST, PORT))     
        while 1:         
            self.socket.listen(1)        
            self.conn, addr = self.socket.accept()        
            self.ectrl_connected()
            
            while 1:
                try:
                    print("aspetto data...") 
                    raw_data = self.conn.recv(32754).strip()
                    if not raw_data: 
                        self.conn.close
                        self.ectrl_disconnected()
                        print("empty data")
                        break
                
                   # print(f'received raw data {raw_data}') 
                    
                    #dispatch dei messaggi 
                    msg = json.loads(raw_data) 
                    print(f"######DEBUG: {msg}")

                    if msg['type'] == SMessage.read():

                    
                    if msg['type'] == SMessage.hellom():
                        data = msg['data'] 
                        self.ectrl_hello(data)
                        print("INVIO TUTTO_OK SIGNAL") 
                        self.__send_data_to_client()
                        
                    if msg['type'] == SMessage.stopm(): 
                        info = msg['data'] 
                        self.ectrl_close(info)
                        break
                    
                    self.conn.sendall(b'OK')
                        
                except:
                    break

    def __send_data_to_client(self, conn, typem, data):
        write_data_msg = {
            "type": typem,
            "data": data
        }
        data = json.dumps(write_data_msg)
        bData = bytes(data)

        print('DEBUG PACKET INFO: ', bData)

        conn.sendall(bData)

m = Service() 
m.host('localhost', 9990)


