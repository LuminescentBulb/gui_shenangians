import numpy

class Calculator:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        if self.y == 0:
            return "Not a number"
        
        return self.x / self.y

    def percent(self):
        return self.x / 100.0
    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def plusminus(self):
        return -1 * self.x
    
