def make_pizza(size, *toppings):
    '''imprime cada pedido de pizza dos argumentos de entrada'''
    print(f'\nMaking a {size} -inch pizza with the followng toppings')
    for topping in toppings:
        print(f'- {topping}') 