prompt = "Boa noite senhores e senhoras!"
prompt += "Desam quantos lugares?: "

number = int(input(prompt))

if number > 8: 
    print(f"Sinto muito, mas não temos mesas com {number} lugares no momento, peço que aguardem um intante :)")
else:
    print("Otimo! espere um momento que irei acomodalos.")
