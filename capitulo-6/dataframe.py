import pandas as pd

# user ={
#     'Nome':['jailson','patricia','gustavo','joão','paulo'],
#     'Idade':[31,27,10,10,65],
#     'Cidade':['santa inês-MA','São Paulo','Bahia','piau','pindaré']
    
# }

# saida = pd.DataFrame(user)

data = 'capitulo-6/arquivo.xlsx'
saida = pd.read_excel(data)
print(saida.head(50))