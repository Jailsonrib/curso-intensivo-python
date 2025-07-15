from random import randint
class Die:
    def __init__(self,a,b):
        self.a = a
        self.b =b 
        self.results =randint(self.a,self.b) 
    def roll_die(self):
        print(self.results)
         
die = Die(1,3000)
die.roll_die()       