import random
class Die:
    def __init__(self,a,b):
        self.a = a
        self.b =b 
        self.results =random.randint(self.a,self.b) 
    def roll_die(self):
        print(self.results)
         

class Loterica:
    def __init__(self):
        ...
        
        
x = [1,4,89,34,21,90,45,32,76,56,79,2,34,13,64,44,66,43,32,56,'a','b','c','d','e','f','g'  ]
  
lista =random.choices(x, k=2)
print(lista)