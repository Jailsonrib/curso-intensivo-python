def imprimir(lista_pendente):
    
    while lista_pendente:
        imprimindo = lista_pendente.pop()
        print('Imprimindo...: ',imprimindo)
        lista_completa.append(imprimindo)
    
def mostrando_concluidos(lista_completa):
    
    for completa in lista_completa:
        
        print('Itens impressos: ',completa)
        
lista_pendente = ['Banners','cartão presente','fotografias']
lista_completa = []

imprimir(lista_pendente[:])
mostrando_concluidos(lista_completa)

       