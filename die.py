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
        self.num = [letra + str(numero) for letra in string.ascii_lowercase for numero in string.digits]


    def show_num(self):
        print("Qualquer bilhete que corresponder a estes números ganhará 1 milhão :".upper() ,"['r1', 't5', 'z6', 'e0']\n")
        self.ra = random.choices(self.num, k=4)
        print(self.ra)      
        
        
  
na = Loterica()
na.show_num()

np = Die(12,555)
np.roll_die()

