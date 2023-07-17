from messages import SMessage
import json 
import numpy as np
import socket




class Simulator: 
    def __init__(self, host, port):
        self.host = host 
        self.port = port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.host, self.port))
        self.action = None

    def init_sim(self):
        print("qua ci va l'inizializzazione")
        pass

    def __send_data_to_client(self, typem, data):
        write_data_msg = {
            "type": typem,
            "data": data
        }
        data = json.dumps(write_data_msg)
        bData = bytes(data, 'utf-8')

        self.conn.sendall(bData)
    
    def compute_new_state(self, dummy_action=None): 
        #logica del nuovo stato -- dummy random 
        return np.random.normal(0.5, 0.1) 
        
    def run_sim(self): 
        #ciclo principale client
        

        print("simulatore connesso")

        self.init_sim()
        
        while True: 
            # Call READ -- receive action from Agent
            self.__send_data_to_client(SMessage.readm(), 'write_tags' )
            raw_data = self.conn.recv(32754).strip()
            action_data = json.loads(raw_data)

            new_state = self.compute_new_state(action_data['data'])

            # WRITE -- send new state to controller
            self.__send_data_to_client(SMessage.readm(), 'new_state')
            self.__send_data_to_client(SMessage.procstep(), 'time_step')




if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9990
    sim = Simulator(HOST, PORT)

    sim.run_sim()
        
        
        
