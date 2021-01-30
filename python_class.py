class Calculator:
    def __init__(self):
        self.result = 3
    
    def add(self, num):
        self.result += num
        return self.result
    
a = Calculator()
print(a.add(3))