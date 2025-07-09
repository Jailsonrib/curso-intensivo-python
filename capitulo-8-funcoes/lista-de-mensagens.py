





def lista():
    mensagens_aleatorias = [
    "Olá! Como você está hoje?",
    "Que o seu dia seja repleto de alegria.",
    "Acredite nos seus sonhos e vá em frente!",
    "Pequenos gestos fazem grandes diferenças.",
    "A vida é uma jornada, aproveite cada passo.",
    "Não se esqueça de sorrir!",
    "Cada dia é uma nova oportunidade.",
    "Mantenha a calma e siga em frente.",
    "A gentileza gera gentileza.",
    "Você é mais forte do que imagina."
    ]
    cop=(mensagens_aleatorias[:])
    cop[3] = 'Essa porra foi alterada'
    print(mensagens_aleatorias)   
    
    return cop



def show_messages(mensagens=''):
    for indices, message in enumerate(mensagens):
        print(indices + 1, message)
   
               
    
   
   
   
    
def enviar_mensag():
    lista_de_compras = ["pão", "leite", "ovos", 123 + 12, (4)**2]
    return lista_de_compras




show_messages(lista())
show_messages(enviar_mensag())


    
   
    
    
    

    