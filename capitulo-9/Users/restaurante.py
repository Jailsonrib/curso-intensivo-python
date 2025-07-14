from userAdmin import UserAdmin

class Restaurante:
    """
    Define a classe Restaurante, que representa um restaurante
    com suas características e funcionalidades.
    """

    def __init__(self, restaurante_nome, cuisine_type):
        # Inicializa o nome do restaurante e o tipo de culinária
        self.restaurante_nome = restaurante_nome  
        self.cuisine_type = cuisine_type
        
    def describe_restaurante(self):
        # Imprime o nome e o tipo de culinária do restaurante
        print(f"Restaurante: {self.restaurante_nome}")
        print(f"Tipo de culinária: {self.cuisine_type}")


    def open_restaurante(self):
        # Imprime uma mensagem indicando que o restaurante está aberto
        print(f"{self.restaurante_nome} está aberto!")

    def number_served(self, number=0):
        # Define ou imprime o número de clientes atendidos
        if number > 0:
            print(f"Número de clientes atendidos: {number}")
        else:
            print("Nenhum cliente atendido ainda.")
        self.number_served = number 

    def increment_number_served(self, number_increment=0):
        # Incrementa o número de clientes atendidos
        if not hasattr(self, 'number_served'):
            print("Erro: O número de clientes atendidos ainda não foi definido.")
            return

        if number_increment >= 0:
            # OPERAÇÃO SOBRE O ATRIBUTO: Adiciona o incremento ao valor atual de 'self.number_served'.
            self.number_served += number_increment
            print(f"Número de clientes atendidos atualizado para: {self.number_served}")
        else:
            print("O número de clientes atendidos não pode ser negativo.")

class IceScreamStand(Restaurante):
    """
    Classe IceCreamStand herda de Restaurante e representa um restaurante especializado em sorvetes.
    """
    def __init__(self, restaurante_nome, cuisine_type):
        """
        Inicializa os atributos da classe pai e define o tipo de culinária como 'Sorvete'.
        """
        super().__init__(restaurante_nome, cuisine_type)  # Chama o construtor da classe pai
        self.flavors = [] # Inicializa uma lista vazia para armazenar os sabores de sorvete
        

    def add_flavor(self, flavor):
        """
        Adiciona um novo sabor à lista de sabores disponíveis.
        """
        self.flavors.append(flavor)
      
    def show_flavors(self):
        # Imprime todos os sabores de sorvete disponíveis
        print("Sabores disponíveis:")
        for flavor in self.flavors:
            print(f"- {flavor} ")
        

# Cria uma instância da classe IceScreamStand
restaurant = IceScreamStand("Sorveteria do João", "Sorveteria")

# Cria uma instância da classe UserAdmin (assumindo que 'UserAdmin' está definida em 'userAdmin.py')
user1 = UserAdmin("josé",'ribeiro','31','1.78','83')
# Define os privilégios do usuário
user1.privileges = ["Pode adicionar postagens", "Pode deletar postagens", "Pode banir usuários"]
# Imprime a descrição do usuário
print(user1.describe_user())
# Imprime os privilégios do usuário
print(user1.show_privileges())


# Adiciona sabores de sorvete ao restaurante
restaurant.add_flavor("Chocolate,Morango, Creme com passas")  
# Exibe os sabores de sorvete disponíveis
restaurant.show_flavors()