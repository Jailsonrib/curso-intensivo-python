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
        return long_name.title()

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
            
            
            
my_new_car = Car('audi', 'a4', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(122)
my_new_car.increment_odometer(20)
my_new_car.read_odometer()
    