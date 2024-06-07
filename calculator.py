import numpy

class Calculator:
    def __init__(self):
        self.operation = ""
        self.x = 0
        self.y = 0
    
    def evaluate(self):
        if self.operation == "":
            return
        
        if self.operation == "multiply":
            self.x = self.x * self.y
            self.y = 0
            return self.x
        
        if self.operation == "divide":
            self.x = self.x / self.y
            self.y = 0
            return self.x