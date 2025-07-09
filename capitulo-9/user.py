class User:
    def __init__(self, first_name, last_name, age, altura=None, peso=None, ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.altura = altura
        self.peso = peso
        self.attempts = 0
        # Atributos de instância: Guarda informações sobre o usuário.
    # A função construtora __init__ inicializa os atributos do usuário, como nome, sobrenome, idade, altura e peso.
    def describe_user(self):
        self.datas_user = (f"""\tNome: {self.first_name} {self.last_name},
        Idade: {self.age} anos
        altura: {self.altura} cm
        Peso: {self.peso} kg""".title())
        print(self.datas_user)
        
    def increment_login_attempts(self):
        if self.datas_user:
        
            
            self.attempts += 1
            
            print(f"\tTentativas de login: {self.attempts}")
    
    def reset_login_attempts(self, reset=0):
      
            self.attempts -= reset

            print(f'entativas de login reiniciadas.   {self.attempts}')
        
    def greet_user(self):
        print(f"\tOlá, {self.first_name} {self.last_name}!")
        
great = User("João", "Silva", 30)
great2 = User("Maria", "Oliveira", 25, altura=170, peso=65)
great.greet_user()
great.describe_user()
great.increment_login_attempts()

great2.greet_user()
great2.describe_user()
great2.increment_login_attempts()
great.increment_login_attempts()
# great2.reset_login_attempts(1)
great2.increment_login_attempts()
great2.increment_login_attempts()
great2.reset_login_attempts(2)
great2.increment_login_attempts()


