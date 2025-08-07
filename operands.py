class Operands:

    def __init__(self, num):
        self.num = num


    def __str__(self):
        return f"{self.num}"
    
    def __add__(self, other):
        self.temp_num = self.num + other.num
        return f"{self.temp_num}"
    
    def __sub__(self, other):
        self.temp_num = self.num - other.num
        return f"{self.temp_num}"
    
    def __mul__(self, other):
        self.temp_num = self.num * other.num
        return f"{self.temp_num}"