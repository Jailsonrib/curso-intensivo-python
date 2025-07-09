responses={}

flag =True
while flag:
    name = input('Qual o seu nome: ')
    response = input('what animal would you like to hava ?')


    responses[name] = response
    question = input('Do you whant to continue whith questions (S/N) ? ').lower()
    if question == 'n':
        flag = False

    print(responses)