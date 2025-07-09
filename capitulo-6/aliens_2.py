# alien_0 = {'color':'green', 'points':5}
# alien_1 = {'color':'yellow', 'points':10}
# alien_2 = {'color':'red', 'points':15}

# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     for inf, ali in alien.items():
#         print(inf,ali)
from random import choice
#Cria uma lista vazia        
aliens=[]
lista_cores=['yellow','black','blue','pink','green']

#Cria uma frota com 20 alienigenas
for number_alien in range(20):
    charge_color = choice(lista_cores)
    new_alien= {'color':charge_color, 'points':number_alien,'speed':'alow'}
    aliens.append(new_alien)
for al in aliens[-10:-2]:
    print(al)
