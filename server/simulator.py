from messages import SMessage
import json 
import numpy as np 



class Simulator: 
    def __init__(self, host, port) 
        self.host = host 
        self.port = port 
        
    def init_sim(self) 
        pass 
    
    
    def compute_new_state(self, dummy_action=None): 
        #logica del nuovo stato -- dummy random 
        return np.random.normal(0.5, 0.1) 
        
    def run_sim(self): 
        #ciclo principale client
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.host, self.port) 
        print("simulatore connesso") 
        
        while True: 
            #Call READ -- receive action from Agent
            s.send(bytes(Smessage.readm()) 
                   
            #compute new 
            self.state = compute_new_state() 
            
            #communicate the new state 
            s.send(
            
            
        
        
        
