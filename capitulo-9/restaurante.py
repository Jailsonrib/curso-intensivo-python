class Restaurante:
    """
    Define a classe Restaurante, que representa um restaurante
    com suas características e funcionalidades.
    """

    def __init__(self, restaurante_nome, cuisine_type):
        """
        Método construtor da classe Restaurante.
        É chamado automaticamente toda vez que um novo objeto Restaurante é criado.

        Args:
            restaurante_nome (str): O nome do restaurante.
            cuisine_type (str): O tipo de culinária que o restaurante oferece.
        """
        self.restaurante_nome = restaurante_nome  # Atributo de instância: guarda o nome do restaurante
        self.cuisine_type = cuisine_type          # Atributo de instância: guarda o tipo de culinária
        # self.number_served = 0 # É uma boa prática inicializar atributos numéricos aqui,
                                # caso não sejam definidos por outro método imediatamente.
                                # No seu código original, ele é criado em 'number_served()'.

    def describe_restaurante(self):
        """
        Método que imprime na tela o nome e o tipo de culinária do restaurante.
        Acessa os atributos de instância 'restaurante_nome' e 'cuisine_type'.
        """
        print(f"Restaurante: {self.restaurante_nome}")
        print(f"Tipo de culinária: {self.cuisine_type}")

    def open_restaurante(self):
        """
        Método que simula a abertura do restaurante, imprimindo uma mensagem.
        """
        print(f"{self.restaurante_nome} está aberto!")

    def number_served(self, number=0):
        """
        Este método tem uma dupla função no seu código:
        1. Imprime o número de clientes que 'foram atendidos'.
        2. Define/Atualiza o atributo de instância 'self.number_served'
           com o valor passado, 'guardando' essa informação no objeto.

        Args:
            number (int): O número de clientes a ser 'atendido' ou definido.
                          O valor padrão é 0.
        """
        if number > 0:
            print(f"Número de clientes atendidos: {number}")
        else:
            print("Nenhum cliente atendido ainda.")
        self.number_served = number  # ATRIBUTO DE INSTÂNCIA: Armazena o 'number'
                                     # como uma característica permanente deste objeto 'Restaurante'.
                                     # Ele persistirá após o método 'number_served()' terminar.

    def increment_number_served(self, number_increment=0):
        """
        Método que incrementa o número total de clientes atendidos.
        Acessa e modifica o atributo de instância 'self.number_served'.

        Args:
            number_increment (int): O valor a ser adicionado ao total de clientes atendidos.
                                    O valor padrão é 0.
        """
        # Verifica se 'self.number_served' existe. Se não foi inicializado antes,
        # geraria um erro se a linha 'self.number_served = number' em 'number_served()'
        # tivesse sido removida.
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
        self.flavors = []  # Atributo para armazenar os sabores de sorvete disponíveis

    def add_flavor(self, flavor):
        """
        Adiciona um novo sabor à lista de sabores disponíveis.
        """
        self.flavors.append(flavor)

    def show_flavors(self):
        """
        Exibe todos os sabores de sorvete disponíveis.
        """
        print("Sabores disponíveis:")
        for flavor in self.flavors:
            print(f"- {flavor}")
# ---

# Cria uma instância (objeto) da classe Restaurante.
# 'restaurant' é agora um objeto que representa a "Pizzaria do João".
restaurant = IceScreamStand("Sorveteria do João", "Sorveteria")
restaurant.describe_restaurante()  # Chama o método para descrever o restaurante.
restaurant.add_flavor("Chocolate,Morango, Creme com passas")  # Adiciona o sabor "Chocolate" ao restaurante.
restaurant.show_flavors()  # Exibe os sabores disponíveis no restaurante.
