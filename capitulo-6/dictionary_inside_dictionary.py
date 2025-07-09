users = {
    'user_0':{
        'first_name':'Jailson',
        'last_name':'Ribeiro',
        'age':31,
        'color':'black'
    },
    'user_1':{
        'first_name':'Patricia',
        'last_name':'Macedo Ribeiro',
        'age':27,
        'color':'brown'
    }
}

for username, infor in users.items():
    
    print(f"""Nome: {infor['first_name']} {infor['last_name']}.
Idade: {infor['age']}
Cor de pele: {infor['color']}""".title())
    
        
   
   