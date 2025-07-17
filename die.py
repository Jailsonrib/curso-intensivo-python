import random
import string
class Die:
    def __init__(self,a,b):
        self.a = a
        self.b =b 
        self.results =random.randint(self.a,self.b) 
    def roll_die(self):
        print(self.results)
         

class Loterica:
    def __init__(self):
       pass 
        
    def rangeNum(self, rangeN):
        self.num = [letra + str(string.digits)
        for letra in string.ascii_lowercase
        for string.digits in range(rangeN)]


    def show_num(self,nf):
        print("Qualquer bilhete que corresponder a estes números ganhará 1 milhão :".upper() ,"['r1', 't5', 'z6', 'e0']\n")
        self.ra = random.choices(self.num, k=nf)
        print(self.ra)      
        
        
  
na = Loterica()
na.rangeNum(3)
na.show_num(4)




