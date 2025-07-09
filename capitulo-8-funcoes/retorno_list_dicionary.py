from datetime import date # Importa a classe 'date' do módulo 'datetime', usada para obter o ano atual.

def get_dates(first_name, last_name, midle_name='', age:int=0,):
    # Esta função recebe um primeiro nome, um sobrenome, um nome do meio opcional e uma idade opcional.
    # Ela calcula a idade com base em um ano de nascimento fixo (1994) e retorna um dicionário
    # contendo os detalhes da pessoa.

    right_year = date.today().year # Obtém o ano atual usando date.today().year.
    age = right_year - 1994 # Calcula a idade subtraindo 1994 (ano de nascimento assumido) do ano atual.

    person = {'first_name':first_name, # Cria um dicionário para armazenar as informações da pessoa.
    'last_name':last_name,
    'age':age}

    if midle_name.strip():
        # Verifica se 'midle_name' não está vazio após remover espaços em branco no início/fim.
        # Isso garante que um nome do meio seja adicionado apenas se for realmente fornecido.
        person['midle_name'] = midle_name # Adiciona o 'midle_name' ao dicionário se ele existir.
    return person # Retorna o dicionário contendo os detalhes da pessoa.

4
def charged():
    # Esta função chama 'get_dates' para obter as informações de uma pessoa e então
    # imprime cada par chave-valor do dicionário retornado.

    full_name = get_dates('jailson','macedo','pêndolas') # Chama 'get_dates' com valores de nome específicos.

    for k,v in full_name.items():
        # Itera por cada par chave-valor no dicionário 'full_name'.
        print(k.title(), ':',v) # Imprime a chave (com a primeira letra maiúscula) e seu valor correspondente.

charged() # Chama a função 'charged' para executar o código.