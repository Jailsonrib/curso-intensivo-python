class Car:
    """
    Representa um carro.
    """
    def __init__(self, make, model, year):
        """
        Inicializa os atributos do carro.
        :param make: A marca do carro (ex: 'Toyota').
        :param model: O modelo do carro (ex: 'Corolla').
        :param year: O ano de fabricação do carro (ex: 2023).
        """
        self.make = make             # Atributo para armazenar a marca do carro.
        self.model = model           # Atributo para armazenar o modelo do carro.
        self.year = year             # Atributo para armazenar o ano do carro.
        self.odometer_reading = 0    # Atributo para armazenar a quilometragem do carro, inicializado em 0.

    def get_descriptive_name(self):
        """
        Retorna uma descrição legível do carro, formatada com ano, marca e modelo.
        """
        long_name = f"Informações do veículo: ano: {self.year} marca: {self.make} modelo: {self.model}"
        print(long_name.title())     # Imprime a descrição do carro com a primeira letra de cada palavra em maiúscula.

    def read_odometer(self):
        """
        Exibe a quilometragem atual do carro.
        """
        print(f"Este carro tem {self.odometer_reading} milhas no odômetro.") # Imprime a quilometragem.

    def update_odometer(self, mileage=0):
        """
        Define o valor do odômetro. Este método evita que o odômetro seja revertido para um valor menor.
        :param mileage: O novo valor da quilometragem para o odômetro. O padrão é 0.
        """
        if mileage >= self.odometer_reading: # Verifica se a nova quilometragem é maior ou igual à atual.
            self.odometer_reading = mileage  # Atualiza o odômetro com a nova quilometragem.
        elif mileage < self.odometer_reading and mileage != 0: # Se a nova quilometragem for menor (e diferente de 0).
            print("Você não pode reverter o odômetro!") # Impede a reversão do odômetro.

    def fiill_gas_tank(self):
        """
        Exibe uma mensagem informando que o tanque de combustível foi cheio.
        Este método é específico para carros a gasolina e será sobrescrito em classes filhas como ElectricCar.
        """
        print("O tanque de combustível foi cheio.") # Mensagem de confirmação.

    def increment_odometer(self, miles=0):
        """
        Incrementa o valor do odômetro adicionando uma quantidade de milhas.
        Este método evita que o odômetro seja diminuído.
        :param miles: A quantidade de milhas a ser adicionada ao odômetro. O padrão é 0.
        """
        if miles >= 0 and miles != 0:  # Verifica se as milhas a serem adicionadas são positivas e diferentes de zero.
            self.odometer_reading += miles # Adiciona as milhas ao odômetro atual.
        else:
            print("Você não pode diminuir o odômetro!") # Impede a diminuição do odômetro.