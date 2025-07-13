from user import User 

class UserAdmin(User):
    def __init__(self,first_name, last_name, age, altura=None, peso=None):
        super().__init__(first_name, last_name, age, altura, peso)
        self.privileges = []
    def show_privileges(self):
        if self.privileges:
            print(f"\t{self.first_name} {self.last_name} tem os seguintes privilégios:")
            for i, privilege in enumerate(self.privileges, start=1):
                
                print(f"\t- {privilege} {i}")
        else:
            print(f"\t{self.first_name} {self.last_name} não tem privilégios.")
user = UserAdmin("Carlos", "Pereira", 28, altura=180, peso=75)
user.describe_user()
user.privileges = ["Pode adicionar postagens", "Pode deletar postagens", "Pode banir usuários"]
user.show_privileges()
user.privileges = ["Pode adicionar postagens", "Pode deletar postagens", "Pode banir usuários"]
user.show_privileges()