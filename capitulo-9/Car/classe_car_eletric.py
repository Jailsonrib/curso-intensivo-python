from class_Battery import Baterry
from class_car import Car

class ElectricCar(Car):
    """Representa aspectos de um carro elétrico, além dos atributos da classe Car."""
    """Inicializa os atributos da classe filha."""
    def __init__(self, make, model, year):
        
        """Inicializa os atributos da classe pai."""
        super().__init__(make, model, year)
        self.battery = Baterry()  # Tamanho da bateria em kWh
        
    def fiill_gas_tank(self):
        print("Este carro não tem tanque de combustível!")


    
            

my_new_car = ElectricCar('audi', 'a4', 2025)
my_new = Car('poco x7 pro', 'apenas teste', 1856)

my_new_car.get_descriptive_name()
my_new_car.battery.battery_life(2)
my_new_car.battery.get_range()