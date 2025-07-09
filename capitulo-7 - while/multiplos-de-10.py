

numero = int(input("Digite o numero para saber se ele é ou não multiplo de 10: "))

resto_div = numero % 10
multi = numero * 10
if numero % 10==0:
    
    print(f"O numero {numero} é multiplo de 10, porque o resto da divisão foi {resto_div} e a multiplicação é {multi}")
else:
    print(f"O numero {numero} não é multiplo de 10, porque o resto da divisão não foi zero e sim {resto_div} e a multiplicação é {multi}")