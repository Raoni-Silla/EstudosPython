
cidades_lista = []

# Abre o arquivo Cidades.txt no modo leitura ('r'), usando UTF-8 para suportar acentuação
with open('Cidades.txt', 'r', encoding='utf-8') as cidades:
    # O 'for' percorre o arquivo linha por linha
    for linha in cidades:
        # Remove quebras de linha/espacos extras e separa os valores por vírgula achada
        dados = linha.strip().split(',')

        # Monta um dicionário representando a cidade
        #
        cidade = {
            'codigo': dados[0],
            'descricao': dados[1],
            'estado': dados[2]
        }

        # Adiciona a cidade à lista principal
        cidades_lista.append(cidade)

# Após o loop, a lista 'cidades_lista' está completa
# Exemplo: [{'codigo': '1', 'descricao': 'São Paulo', 'estado': 'SP'}, {...}, {...}]

# Acessa a primeira cidade da lista
primeira_cidade = cidades_lista[0]
print(f"Primeira cidade: Código: {primeira_cidade['codigo']} | Descrição: {primeira_cidade['descricao']}")

# Exibe a lista completa de cidades
print("\nLista completa de cidades:")
print(cidades_lista)
