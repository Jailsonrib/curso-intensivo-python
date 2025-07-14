from user import User


class UserAdmin(User):
    def __init__(self,first_name=None, last_name=None, age=None, altura=None, peso=None, ):
        super().__init__(first_name=None, last_name=None, age=None, altura=None, peso=None, )
        self.privileges = []
    def show_privileges(self):
        if self.privileges:
            print(f"\t{self.first_name} {self.last_name} tem os seguintes privilégios:")
            for i, privilege in enumerate(self.privileges, start=1):
                
                print(f"\t- {privilege} {i}")
        else:
            print(f"\t{self.first_name} {self.last_name} não tem privilégios.")
# user = UserAdmin()
# # user.describe_user()
# user.privileges = ["Pode adicionar postagens", "Pode deletar postagens", "Pode banir usuários"]
# user.show_privileges()
