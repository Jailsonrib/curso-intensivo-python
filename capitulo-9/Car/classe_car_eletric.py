from class_Battery import Baterry  # Importa a classe Baterry do arquivo 'class_Battery'.
from class_car import Car          # Importa a classe Car do arquivo 'class_car'.

class ElectricCar(Car):
    """
    Representa aspectos de um carro elétrico, além dos atributos da classe Car.
    """
    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe filha.
        Inicializa os atributos da classe pai.
        """
        super().__init__(make, model, year)  # Chama o método __init__ da classe pai (Car)
                                             # para inicializar seus atributos (make, model, year).
        self.battery = Baterry()             # Cria uma nova instância da classe Baterry e
                                             # a atribui ao atributo 'battery' do ElectricCar.

    def fiill_gas_tank(self):
        """
        Sobrescreve o método fiill_gas_tank da classe pai Car.
        Um carro elétrico não possui tanque de combustível, então este método imprime uma mensagem informativa.
        """
        print("Este carro não tem tanque de combustível!")


# --- Instanciação de Objetos e Chamadas de Métodos ---

my_new_car = ElectricCar('audi', 'a4', 2025)  # Cria uma instância da classe ElectricCar.
my_new = Car('poco x7 pro', 'apenas teste', 1856) # Cria uma instância da classe Car.

my_new_car.get_descriptive_name()  # Chama o método get_descriptive_name (herdado de Car)
                                   # no objeto my_new_car para imprimir seu nome descritivo.

my_new_car.battery.battery_life(202)  # Acessa o atributo 'battery' de my_new_car (que é um objeto Baterry)
                                     # e chama seu método battery_life com o argumento 202.

my_new_car.battery.get_range()      # Acessa o atributo 'battery' de my_new_car e
                                     # chama seu método get_range para exibir o alcance do carro.