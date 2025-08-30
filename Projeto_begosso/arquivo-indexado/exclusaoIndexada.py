class indice:
    def __init__(self, codigo, posicao):
        self.esquerda = None
        self.direita = None
        self.codigo = codigo
        self.posicao = posicao

class cliente:
    def __init__(self, codigo, nome, endereco, cidade, uf, estado=1):
        self.estado = estado
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf

def busca(codigo, raiz, area_de_dados):
    while raiz is not None:
        if codigo == raiz.codigo:
            cliente_encontrado = area_de_dados[raiz.posicao]
            if cliente_encontrado.estado != 0:
                print(f"Código achado com sucesso! Procurado {codigo}, encontrado {raiz.codigo}")
                return raiz
            else:
                print(f"Código {codigo} encontrado, mas o cliente está logicamente excluído.")
                return None
        elif codigo < raiz.codigo:
            raiz = raiz.esquerda
        else:
            raiz = raiz.direita
    print("Código não encontrado")
    return None

def include(raiz, codigo, posicao):
    if raiz is None:
        return indice(codigo, posicao)

    if codigo > raiz.codigo:
        raiz.direita = include(raiz.direita, codigo, posicao)
    else:
        raiz.esquerda = include(raiz.esquerda, codigo, posicao)

    return raiz

def delete(raiz, codigo, area_de_dados):
    verificador = busca(codigo, raiz, area_de_dados)
    if verificador is not None:
        cliente_excluir = area_de_dados[verificador.posicao]
        cliente_excluir.estado = 0
        print(f"Cliente com código {codigo} excluído logicamente.")
    else:
        print(f"Cliente com código {codigo} não encontrado ou já excluído.")

def main():
    raiz = None
    area_de_dados = []



    while True:
        print('-=-' * 20)
        opcao = int(input('Digite a opção desejada (1=buscar, 2=inserir, 3=excluir, 0=sair): '))
        print('-=-' * 20)

        match opcao:
            case 1:
                codigobuscado = int(input('Digite o código que você deseja buscar: '))
                busca(codigobuscado, raiz, area_de_dados)

            case 2:
                codigoInserido = int(input('Digite o número que deseja inserir: '))
                nova_posicao = len(area_de_dados)
                area_de_dados.append(cliente(codigoInserido, "Novo Cliente", "...", "...", "..."))
                raiz = include(raiz, codigoInserido, nova_posicao)
                print(f"Código {codigoInserido} inserido com sucesso!")

            case 3:
                codigoExcluir = int(input('Digite o código que você deseja excluir: '))
                delete(raiz, codigoExcluir, area_de_dados)

            case 0:
                print("Saindo do programa...")
                break

if __name__ == "__main__":
    main()