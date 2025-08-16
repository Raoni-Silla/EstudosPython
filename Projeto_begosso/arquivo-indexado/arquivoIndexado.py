


class indice:
    def __init__(self, codigo, posicao):
        self.esquerda = None
        self.direita =  None # começa sendo vazio
        self.codigo =  codigo
        self.posicao = posicao

class cliente:
    def __init__(self, codigo, nome, endereco, cidade, uf):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade =  cidade
        self.uf = uf


def busca (codigo, raiz):

    while raiz is not None:
      if codigo == raiz.codigo:
          print("Código achado com sucesso, codigo {} e codigo achado {}".format(codigo, raiz.codigo))
          return raiz
      elif codigo < raiz.codigo:
        raiz = raiz.esquerda
      else:
          raiz = raiz.direita
    print("codigo não encontrado")
    return None






def main ():
    raiz = None
    print('-=-' * 20)
    opcao = int(input('Digite a opção desejada: '))
    print('-=-'* 20)
    match opcao:
        case 1:
            print('-=-' * 20)
            codigobuscado = int(input('Digite o codigo que você deseja buscar: '))
            print('-=-' * 20)
            busca (codigobuscado,raiz)
