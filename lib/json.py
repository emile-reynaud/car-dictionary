# json.py

import os
import json

class JSON:
    
    file = 'data/default.json'
    data = {}
    
    def __init__(self, file:str):
        if os.path.exists(file):
            self.file = file
        else:
            with open(file, 'x') as file:
                self.file = file
                file.close()
                
    def __call__(self):
        with open(self.file, 'r') as file:
            print(json.load(file))
            file.close()
            
    def load(self):
        with open(self.file, 'r') as file:
            self.data = json.load(file)
            file.close()
            
    def write(self):
        with open(self.file, 'w') as file:
            file.write(json.dumps(self.data, indent=4))
            file.close()
            
    def write(self, data:dict):
        with open(self.file, 'w') as file:
            file.write(json.dumps(data, indent=4))
            file.close()