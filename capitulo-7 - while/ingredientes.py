ingredi_add = []
TAG = True
while TAG:
    prompt = """Cardapio:
    - Mussarela
    -Nodestina 
    - queijos\n"""
    prompt += 'Digite os ingredientes. Caso desejar sair digite(S)'.lower()
    ingredientes = input(prompt)
    if ingredientes == 's':
            TAG = False
    if ingredientes != 's':
        ingredi_add.append(ingredientes)
        
print(ingredi_add)