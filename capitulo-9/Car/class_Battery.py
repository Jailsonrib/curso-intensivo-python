class Baterry:
    """
    Representa uma bateria de carro.
    """
    def __init__(self, battery_size=0):
        """
        Inicializa os atributos da bateria.
        :param battery_size: O tamanho da bateria em kWh. O valor padrão é 0.
        """
        self.battery_size = battery_size  # Atributo que armazena o tamanho da bateria.

    def battery_life(self, battery=0):
        """
        Exibe a capacidade da bateria. Se um novo valor for fornecido, atualiza o tamanho da bateria.
        :param battery: Opcional. Um novo valor para o tamanho da bateria em kWh.
        """
        if battery != 0:
            self.battery_size = battery  # Atualiza o tamanho da bateria se um novo valor for passado.
        print(f"Esta bateria tem {self.battery_size} kWh.") # Imprime a capacidade atual da bateria.

    def get_range(self):
        """
        Calcula e exibe a autonomia da bateria (quantos quilômetros o carro pode percorrer).
        A autonomia é determinada com base no tamanho da bateria.
        """
        if self.battery_size <= 40 and self.battery_size > 0:
            range = 50  # Define o alcance para baterias de até 40 kWh (e maiores que 0).
        elif self.battery_size == 0:
            range = 0   # Bateria de tamanho 0 tem alcance 0.
        elif self.battery_size <= 100:
            range = 150 # Define o alcance para baterias de até 100 kWh.
        else:
            range = 200 # Define o alcance para baterias maiores que 100 kWh.
        print(f"Esta bateria pode ir até {range} km com uma carga completa.") # Imprime a autonomia calculada.