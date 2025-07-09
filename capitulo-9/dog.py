class Dog:
    def __init__(self, name, age):
        # Esta é a função construtora da classe Dog, que inicializa os atributos 'name' e 'age'.
        # 'name' é o nome do cachorro e 'age' é a idade do cachorro
        self.name = name
        self.age = age
        
        
    def sit(self):
        # Este método faz o cachorro sentar e imprime uma mensagem.
        print(f"{self.name} está sentado.")
        
        
    def roll_over(self):
        # Este método faz o cachorro rolar e imprime uma mensagem.
        print(f"{self.name} está rolando.")
dog1 = Dog("Rex", 5)

print(dog1.name)