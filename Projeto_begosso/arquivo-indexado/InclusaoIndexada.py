class indice:
    def __init__(self, codigo, posicao):
        self.esquerda = None
        self.direita = None
        self.codigo = codigo
        self.posicao = posicao

class cliente:
    def __init__(self, codigo, nome, endereco, cidade, uf):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf


def busca(codigo, raiz):
    while raiz is not None:
        if codigo == raiz.codigo:
            print("Código achado com sucesso! Procurado {}, encontrado {}".format(codigo,raiz.codigo))
            return raiz
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


def main():
    raiz = None

    while True:
        print('-=-' * 20)
        opcao = int(input('Digite a opção desejada (1=buscar, 2=inserir, 0=sair): '))
        print('-=-' * 20)

        match opcao:
            case 1:
                codigobuscado = int(input('Digite o código que você deseja buscar: '))
                busca(codigobuscado, raiz)

            case 2:
                codigoInserido = int(input('Digite o número que deseja inserir: '))
                posicao = int(input('Digite a posição: '))
                raiz = include(raiz, codigoInserido, posicao)
                print(f"Código {codigoInserido} inserido com sucesso!")

            case 0:
                print("Saindo do programa...")
                break
