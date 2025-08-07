class Fraction:
    
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, others):
        self.temp_num = self.num * others.den + self.den * others.num
        self.temp_den = self.den * others.den
        self.temp_add = self.temp_num / self.temp_den
        return f"Result : {self.temp_add}"
    
    def __sub__(self, others):
        self.temp_num = self.num * others.den - self.den * others.num
        self.temp_den = self.den * others.den
        return f"Result : {self.temp_num}/{self.temp_den}"
    
    def __mul__(self, others):
        self.temp_num = self.num * others.num
        self.temp_den = self.den * others.den
        return f"Result : {self.num}/{self.temp_den}"
    
    def __truediv__(self, other):
        self.temp_num = self.num * other.den
        self.temp_den = self.den * other.num
        self.temp_div = self.temp_num / self.temp_den
        return f"Result : {self.temp_div}"
    
    #---------------------METHOD------------------------------
    
    def add(self, others):
        self.temp_num = self.num * others.den + self.den * others.num
        self.temp_den = self.den * others.den
        self.temp_add = self.temp_num / self.temp_den
        return f"Result : {self.temp_add}"
    
    def sub(self, others):
        self.temp_num = self.num * others.den - self.den * others.num
        self.temp_den = self.den * others.den
        return f"Result : {self.temp_num}/{self.temp_den}"
    
    def mul(self, others):
        self.temp_num = self.num * others.num
        self.temp_den = self.den * others.den
        return f"Result : {self.num}/{self.temp_den}"
    
    def truediv(self, other):
        self.temp_num = self.num * other.den
        self.temp_den = self.den * other.num
        self.temp_div = self.temp_num / self.temp_den
        return f"Result : {self.temp_div}"
    


   # four type of selector
   # universal selector  =  *{}
   # element selector    =  h1{}
   # id selector         =  #{}
   # class selector      = .class_name