# Lista inicial de animais (com duplicatas)
pets = ['cat','dog','giraf','elephant','monkey','cat','cat','cat','dog']

# Lista vazia para receber os itens
test = []

# Loop para mover todos os itens de 'pets' para 'test'
while pets:
    # Remove o último item de 'pets' e o adiciona à lista 'test'
    test.append(pets.pop())

# Converte a lista 'test' em um 'set' para remover duplicatas
value = set(test)

# Imprime a lista 'test', que agora contém os itens em ordem invertida
print('Lista', test)

# Imprime o 'set' 'value', mostrando apenas os itens únicos
print('conjuntos', value)