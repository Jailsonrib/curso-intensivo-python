#Começa com usuários que precisam ser verificados
#e uma lista vazia a fim de armazanar os usuários confirmados
uncofirmed_users = ['jailson','patricia','João','gustavo']
confirmed_users=[]
#faz a verificação de cada usuário até que não se tenha mais
#usuários não confirmados
#Transfere cada usuário verificado para a lista de usuários confirmados
while uncofirmed_users:
    #Remove cada elemento do final da lista
    current_user = uncofirmed_users.pop()
    #printa cada elemento removido
    print(f'Confirmando : {current_user.title()}')
    #add cada elemento a lista de usuarios confirmados
    confirmed_users.append(current_user)
    #printa todos os elementos usando o metodo .join()
print('Usuários confirmados:',', '.join(confirmed_users))
   
 