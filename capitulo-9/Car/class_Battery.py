class Baterry:
    """Representa uma bateria de carro."""
    def __init__(self, battery_size=0):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def battery_life(self,battery=0):
        """Exibe a capacidade da bateria."""
        if battery != 0:
            self.battery_size = battery
        print(f"Esta bateria tem {self.battery_size} kWh.")
         
    def get_range(self):
        """Exibe a autonomia da bateria."""
        if self.battery_size <= 40 and self.battery_size > 0:
            range = 50
        elif self.battery_size == 0:
            range = 0
        elif self.battery_size <= 100:
            range = 150
        else:
            range = 200
        print(f"Esta bateria pode ir até {range} km com uma carga completa.")     