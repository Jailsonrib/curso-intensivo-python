def make_album ():
    
    artista= input('Qual o nome do artista: ')
    album = input('Qual o nome do album: ')
    
    essencia = {
    'Artista':artista,
    'Album':album,
    }
    lista_de_musicas = []
    
    for i in range(2):
        musicas = input(f'Musica: {i+1} ')
     
        lista_de_musicas.append(musicas)
        
    essencia['Musicas']=lista_de_musicas
         
    return essencia

def mensagem_limpa():
    album_completo = make_album()

    for k,v in album_completo.items():
        if k == 'Musicas':
            lista_musica = ', '.join(v) 
            print('Musicas: ',lista_musica.title())
            continue
        else:
            print(f'{k}: {v.title()}')
    
mensagem_limpa()
    