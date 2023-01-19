# xml.py

import os
from xml.etree.ElementTree import *
from lxml import etree

class XML:
    
    file = 'data/default.xml'
    parser = etree.XMLParser(recover=True)
    data = {}
    
    def __init__(self, file:str):
        if os.path.exists(file):
            self.file = file
        else:
            with open(file, 'x') as file:
                self.file = file
                file.close()
                
    def load(self):
        tree = parse(self.file, parser=self.parser)
        root = tree.getroot()
        
        self.data[root.tag] = root.attrib
        
        for parent in root:
            self.data[parent.tag] = {}
        for parent in root:
            self.data[parent.tag][parent.text] = parent.attrib