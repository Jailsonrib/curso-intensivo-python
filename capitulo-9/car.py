class Car:
    def __init__(self, make, model, year):
        """Inicializa os atributos do carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna uma descrição legível do carro."""
        long_name = f"Informações do veículo: ano: {self.year} marca: {self.make} modelo: {self.model}"
        print(long_name.title())

    def read_odometer(self):
        """Exibe a quilometragem do carro."""
        print(f"Este carro tem {self.odometer_reading} milhas no odômetro.")
       
    def update_odometer(self, mileage=0):
        """Define o valor do odômetro."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            
            
        elif mileage < self.odometer_reading and mileage != 0:
            print("Você não pode reverter o odômetro!") 
            
              
    def increment_odometer(self, miles = 0):
        """Incrementa o valor do odômetro."""
        if miles >= 0 and miles != 0:
            self.odometer_reading += miles
        else:
            print("Você não pode diminuir o odômetro!")
            
class ElectricCar(Car):
    """Representa aspectos de um carro elétrico, além dos atributos da classe Car."""
    """Inicializa os atributos da classe filha."""
    def __init__(self, make, model, year):
        
        """Inicializa os atributos da classe pai."""
        super().__init__(make, model, year)
        self.battery_size = 85  # Tamanho da bateria em kWh

    def describe_battery(self):
        """Exibe a capacidade da bateria do carro elétrico."""
        print(f"Este carro tem uma bateria de {self.battery_size} kWh.")            
            
my_new_car = ElectricCar('audi', 'a4', 2025)
my_new_car.get_descriptive_name()
my_new_car.describe_battery()
my_new_car.read_odometer()
my_new_car.update_odometer(100)
my_new_car.read_odometer()