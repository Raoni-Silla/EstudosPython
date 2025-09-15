# --- TRABALHO PRÁTICO DE ESTRUTURA DE DADOS ---

# Importamos as ferramentas para trabalhar com datas
# 'date' para datas (dia, mês, ano)
# 'timedelta' para somar dias a uma data
# 'datetime' para converter texto em data
from datetime import date, timedelta, datetime
# Nomes dos arquivos que vamos usar para guardar os dados.
#mais facil trabalhar assim do que ficar sempre chamando o txt tipo autores.txt
arquivo_cidades = "cidades.txt"
arquivos_cursos = "cursos.txt"
arquivo_autores = "autores.txt"
arquivos_categorias = "categorias.txt"
arquivos_alunos = "alunos.txt"
arquivos_livros = "livros.txt"
arquivos_emprestimos = "emprestimos.txt"

# Nossas árvores de índice, que guardam os códigos para busca rápida.
# Elas começam vazias ('None').
raiz_cidades = None
raiz_cursos = None
raiz_autores = None
raiz_categorias = None
raiz_alunos = None
raiz_livros = None
raiz_emprestimos = None


# --- Classes: Os "Moldes" para os nossos Dados ---
# aparentemente funciona como no java, sendo apenas o molde pra nossa instancia

class NoArvore:
    # Este é o molde para cada "nó" (galho) da nossa árvore de índice.
    def __init__(self, codigo, posicao):
        self.esquerda = None  # O filho da esquerda na árvore (menor que o pai)
        self.direita = None  # O filho da direita na árvore (maior que o pai)
        self.codigo = int(codigo)  # O código (ex: código do aluno)
        self.posicao = int(posicao)  # A posição (número da linha) no arquivo de texto


# --- Funções da Árvore ---

def adicionar_no_arvore(raiz, codigo, posicao):
    # Esta função adiciona um novo nó na nossa árvore de índice.
    if raiz is None:
        # Se chegamos a um galho vazio, criamos o novo nó aqui.
        return NoArvore(codigo, posicao)

    # Se o código for maior, vamos para a direita. Se for menor, para a esquerda.
    if int(codigo) > raiz.codigo:
        raiz.direita = adicionar_no_arvore(raiz.direita, codigo, posicao)
    else:
        raiz.esquerda = adicionar_no_arvore(raiz.esquerda, codigo, posicao)
    return raiz


# REQUISITO 1.2) Consulta de registros das tabelas.
# A função abaixo ajuda a consultar, buscando o código na árvore de índice.
def buscar_na_arvore(raiz, codigo):
    # Busca um código na árvore e retorna o nó (com a posição no arquivo).
    if raiz is None or raiz.codigo == int(codigo):
        # Se achou ou se a árvore está vazia, retorna o resultado.
        return raiz

    # Se o código for maior, busca na direita. Senão, na esquerda.
    if int(codigo) > raiz.codigo:
        return buscar_na_arvore(raiz.direita, codigo)
    return buscar_na_arvore(raiz.esquerda, codigo)


def coletar_nos_em_ordem(raiz, lista_de_nos):
    # Pega todos os nós da árvore em ordem crescente de código.
    if raiz is not None:
        coletar_nos_em_ordem(raiz.esquerda, lista_de_nos)
        lista_de_nos.append(raiz)
        coletar_nos_em_ordem(raiz.direita, lista_de_nos)


# --- Funções Auxiliares Genéricas (para interagir com arquivos) ---

def carregar_indices(nome_arquivo):
    # Esta função lê um arquivo de dados e cria a árvore de índice para ele.
    raiz = None  # Começa com uma árvore vazia
    try:
        # 'with open' abre o arquivo e o fecha automaticamente no final.
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            posicao = 0  # Guarda a posição de cada linha
            for linha in arquivo:
                # Se a linha não estiver em branco...
                if linha.strip():
                    # Quebra a linha no ';' para pegar o código
                    partes = linha.strip().split(';')
                    codigo = int(partes[0])
                    # Adiciona o código e a posição na árvore
                    raiz = adicionar_no_arvore(raiz, codigo, posicao)
                # Atualiza a posição para a próxima linha
                posicao += len(linha.encode('utf-8'))
    except FileNotFoundError:
        # Se o arquivo não existir, nós o criamos vazio.
        open(nome_arquivo, "w", encoding='utf-8').close()
    return raiz  # Retorna a árvore de índice pronta


def buscar_info_linha(nome_arquivo, codigo_procurado):
    # Este é um jeito simples de buscar, mas não muito rápido!
    # Ele lê o arquivo do começo ao fim toda vez que é chamado.
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(';')
                # Compara o código da linha com o que estamos procurando
                if int(partes[0]) == int(codigo_procurado):
                    return linha.strip()  # Retorna a linha inteira se achar
    except FileNotFoundError:
        return None  # Retorna 'None' (nada) se o arquivo não existir
    return None  # Retorna 'None' se não achar o código


# REQUISITO 1.1) Inclusão de novos registros nas tabelas.
# A função abaixo adiciona um novo registro em um arquivo.
def adicionar_registro(nome_arquivo, linha_registro):
    # Adiciona uma nova linha (registro) no final do arquivo.
    # 'a' significa 'append' (adicionar).
    with open(nome_arquivo, "a", encoding='utf-8') as arquivo:
        arquivo.write(linha_registro + "\n")
    print("Registro adicionado com sucesso!")


def atualizar_arquivo(nome_arquivo, linhas_novas):
    # Reescreve o arquivo inteiro com uma lista de linhas.
    # 'w' significa 'write' (escrever, apagando o que tinha antes).
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        arquivo.writelines(linhas_novas)


# --- Funções de Gerenciamento (Menus) ---

def gerenciar_cidades():
    # Esta função cuida do menu de Cidades.
    global raiz_cidades  # Avisa que vamos usar a variável global
    while True:
        print("\n--- Menu Gerenciar Cidades ---")
        print("1. Adicionar Nova Cidade (Requisito 1.1)")
        print("2. Listar Todas as Cidades (Requisito 1.4)")
        print("0. Voltar ao Menu Principal")
        opcao = input(">> Escolha uma opção: ")

        if opcao == '1':
            cod = input("Digite o código da cidade: ")
            desc = input("Digite o nome da cidade: ")
            uf = input("Digite a UF (ex: SP): ")
            linha = f"{cod};{desc};{uf}"
            adicionar_registro(arquivo_cidades, linha)
            # Recarrega o índice para incluir o novo registro
            raiz_cidades = carregar_indices(arquivo_cidades)

        elif opcao == '2':
            print("\n--- Listagem de Cidades ---")
            try:
                with open(arquivo_cidades, "r", encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        print(linha.strip().replace(";", " - "))
            except FileNotFoundError:
                print("Nenhuma cidade cadastrada.")

        elif opcao == '0':
            break  # Quebra o loop e volta para o menu principal
        else:
            print("Opção inválida.")


# As funções para Cursos, Autores e Categorias são quase iguais à de Cidades.
def gerenciar_cursos():
    # Esta função cuida do menu de Cursos.
    global raiz_cursos
    while True:
        print("\n--- Menu Gerenciar Cursos ---")
        print("1. Adicionar Novo Curso (Requisito 1.1)")
        print("2. Listar Todos os Cursos (Requisito 1.4)")
        print("0. Voltar ao Menu Principal")
        opcao = input(">> Escolha uma opção: ")

        if opcao == '1':
            cod = input("Digite o código do curso: ")
            desc = input("Digite o nome do curso: ")
            linha = f"{cod};{desc}"
            adicionar_registro(arquivos_cursos, linha)
            raiz_cursos = carregar_indices(arquivos_cursos)

        elif opcao == '2':
            print("\n--- Listagem de Cursos ---")
            try:
                with open(arquivos_cursos, "r", encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        print(linha.strip().replace(";", " - "))
            except FileNotFoundError:
                print("Nenhum curso cadastrado.")

        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


# REQUISITO 3) Ao exibir um autor na tabela Autores, o programa deverá buscar o
# código da cidade na tabela de Cidades e exibir o nome da cidade e o Estado.
def gerenciar_autores():
    # Esta função cuida do menu de Autores.
    global raiz_autores
    while True:
        print("\n--- Menu Gerenciar Autores ---")
        print("1. Adicionar Novo Autor (Requisito 1.1)")
        print("2. Listar Todos os Autores (Requisito 1.4)")
        print("0. Voltar ao Menu Principal")
        opcao = input(">> Escolha uma opção: ")

        if opcao == '1':
            cod = input("Digite o código do autor: ")
            nome = input("Digite o nome do autor: ")
            cod_cidade = input("Digite o código da cidade do autor: ")
            linha = f"{cod};{nome};{cod_cidade}"
            adicionar_registro(arquivo_autores, linha)
            raiz_autores = carregar_indices(arquivo_autores)

        elif opcao == '2':
            print("\n--- Listagem de Autores ---")
            try:
                with open(arquivo_autores, "r", encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        partes = linha.strip().split(';')
                        # Busca o nome da cidade para mostrar junto
                        cidade_info = buscar_info_linha(arquivo_cidades, partes[2])
                        nome_cidade = cidade_info.split(';')[1] if cidade_info else "N/A"
                        print(f"Cód: {partes[0]}, Nome: {partes[1]}, Cidade: {nome_cidade}")
            except FileNotFoundError:
                print("Nenhum autor cadastrado.")

        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def gerenciar_categorias():
    # Esta função cuida do menu de Categorias.
    global raiz_categorias
    while True:
        print("\n--- Menu Gerenciar Categorias ---")
        print("1. Adicionar Nova Categoria (Requisito 1.1)")
        print("2. Listar Todas as Categorias (Requisito 1.4)")
        print("0. Voltar ao Menu Principal")
        opcao = input(">> Escolha uma opção: ")

        if opcao == '1':
            cod = input("Digite o código da categoria: ")
            desc = input("Digite o nome da categoria: ")
            linha = f"{cod};{desc}"
            adicionar_registro(arquivos_categorias, linha)
            raiz_categorias = carregar_indices(arquivos_categorias)

        elif opcao == '2':
            print("\n--- Listagem de Categorias ---")
            try:
                with open(arquivos_categorias, "r", encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        print(linha.strip().replace(";", " - "))
            except FileNotFoundError:
                print("Nenhuma categoria cadastrada.")

        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


# REQUISITO 2) Ao exibir um aluno na tabela Alunos, o programa deverá buscar o código do curso na tabela de Cursos e exibir a Descrição.
# REQUISITO 2.1) Buscar o código da cidade na tabela de Cidades e exibir a Descrição e o Estado.
def gerenciar_alunos():
    global raiz_alunos
    while True:
        print("\n--- Menu Gerenciar Alunos ---")
        print("1. Adicionar Aluno (Requisito 1.1)")
        print("2. Consultar Aluno Específico (Requisito 1.2)")
        print("3. Listar Todos os Alunos (Requisito 1.4)")
        print("4. Excluir Aluno (Requisito 1.3)")
        print("0. Voltar ao Menu Principal")
        opcao = input(">> Escolha uma opção: ")

        if opcao == '1':
            cod = input("Digite o código do novo aluno: ")
            nome = input("Digite o nome do aluno: ")
            cod_curso = input("Digite o código do curso: ")
            cod_cidade = input("Digite o código da cidade: ")
            linha = f"{cod};{nome};{cod_curso};{cod_cidade};1"  # '1' no final significa 'ativo'
            adicionar_registro(arquivos_alunos, linha)
            raiz_alunos = carregar_indices(arquivos_alunos)

        elif opcao == '2':
            cod = input("Digite o código do aluno para consultar: ")
            # Usamos o índice para achar a linha do aluno, é mais rápido!
            no_aluno = buscar_na_arvore(raiz_alunos, cod)
            if no_aluno:
                with open(arquivos_alunos, "r", encoding='utf-8') as f:
                    f.seek(no_aluno.posicao)
                    linha = f.readline().strip()
                    partes = linha.split(';')
                    if partes[4] == '1':  # Verifica se está ativo
                        # Aqui cumprimos os requisitos 2 e 2.1
                        curso_info = buscar_info_linha(arquivos_cursos, partes[2])
                        cidade_info = buscar_info_linha(arquivo_cidades, partes[3])
                        nome_curso = curso_info.split(';')[1] if curso_info else "N/A"
                        nome_cidade = cidade_info.split(';')[1] if cidade_info else "N/A"
                        print(
                            f"\n-- Dados do Aluno --\nCód: {partes[0]}, Nome: {partes[1]}, Curso: {nome_curso}, Cidade: {nome_cidade}")
                    else:
                        print("Este aluno foi excluído.")
            else:
                print("Aluno não encontrado.")

        elif opcao == '3':
            print("\n--- Listagem de Alunos Ativos ---")
            try:
                with open(arquivos_alunos, "r", encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        partes = linha.strip().split(';')
                        if partes[4] == '1':  # Mostra só se estiver ativo
                            # Aqui também cumprimos os requisitos 2 e 2.1
                            curso_info = buscar_info_linha(arquivos_cursos, partes[2])
                            cidade_info = buscar_info_linha(arquivo_cidades, partes[3])
                            nome_curso = curso_info.split(';')[1] if curso_info else "N/A"
                            nome_cidade = cidade_info.split(';')[1] if cidade_info else "N/A"
                            print(f"Cód: {partes[0]}, Nome: {partes[1]}, Curso: {nome_curso}, Cidade: {nome_cidade}")
            except FileNotFoundError:
                print("Nenhum aluno cadastrado.")

        elif opcao == '4':
            cod = input("Digite o código do aluno para excluir: ")
            # Exclusão Lógica: muda o '1' para '0' no final da linha
            try:
                linhas_arquivo = open(arquivos_alunos, "r", encoding='utf-8').readlines()
                encontrado = False
                for i, linha in enumerate(linhas_arquivo):
                    if linha.strip().split(';')[0] == cod:
                        partes = linha.strip().split(';')
                        partes[4] = "0"
                        linhas_arquivo[i] = ";".join(partes) + "\n"
                        encontrado = True
                        break
                if encontrado:
                    atualizar_arquivo(arquivos_alunos, linhas_arquivo)
                    print("Aluno excluído com sucesso.")
                else:
                    print("Aluno não encontrado.")
            except FileNotFoundError:
                print("Arquivo de alunos não existe.")

        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


# REQUISITO 4) Ao incluir ou consultar dados na Tabela Livros...
# REQUISITO 8) Ler todos os registros da tabela de Livros e exibi-los em ordem crescente de Código do Livro.
def gerenciar_livros():
    global raiz_livros
    while True:
        print("\n--- Menu Gerenciar Livros ---")
        print("1. Adicionar Livro (Requisito 1.1)")
        print("2. Consultar Livro Específico (Requisito 1.2)")
        print("3. Listar Todos os Livros (Requisito 1.4 e 8)")
        print("4. Excluir Livro (Requisito 1.3)")
        print("0. Voltar")
        opcao = input(">> Opção: ")

        if opcao == '1':
            cod = input("Código do Livro: ")
            titulo = input("Título: ")
            cod_autor = input("Código do Autor: ")
            cod_cat = input("Código da Categoria: ")
            ano = input("Ano de Publicação: ")
            # Formato: codigo;titulo;cod_autor;cod_cat;ano;disponibilidade;estado
            linha = f"{cod};{titulo};{cod_autor};{cod_cat};{ano};1;1"  # Disponível e Ativo
            adicionar_registro(arquivos_livros, linha)
            raiz_livros = carregar_indices(arquivos_livros)

        elif opcao == '2' or opcao == '3':
            disponiveis = 0
            emprestados = 0

            if opcao == '2':
                cod_busca = input("Digite o código do livro para consultar: ")
                livros_para_mostrar = [buscar_info_linha(arquivos_livros, cod_busca)]
            else:  # Listar todos em ordem (REQUISITO 8)
                nos_ordenados = []
                coletar_nos_em_ordem(raiz_livros, nos_ordenados)
                livros_para_mostrar = []
                try:
                    with open(arquivos_livros, "r", encoding='utf-8') as f:
                        for no in nos_ordenados:
                            f.seek(no.posicao)
                            livros_para_mostrar.append(f.readline().strip())
                except FileNotFoundError:
                    livros_para_mostrar = []

            print("\n--- Listagem de Livros ---")
            for linha in livros_para_mostrar:
                if not linha: continue
                partes = linha.split(';')
                if partes[6] == '1':  # Se livro está ativo
                    # REQUISITO 4.1) Buscar o código do autor na tabela Autores e exibir o nome do autor...
                    autor_info = buscar_info_linha(arquivo_autores, partes[2])
                    # REQUISITO 4.2) Buscar o código da categoria na tabela Categorias e exibir a descrição da categoria.
                    cat_info = buscar_info_linha(arquivos_categorias, partes[3])
                    nome_autor = autor_info.split(';')[1] if autor_info else "N/A"
                    nome_cat = cat_info.split(';')[1] if cat_info else "N/A"
                    # REQUISITO 4.3) O atributo disponibilidade serve para indicar se o livro está disponível...
                    disponibilidade = "Disponível" if partes[5] == '1' else "Emprestado"

                    if partes[5] == '1':
                        disponiveis += 1
                    else:
                        emprestados += 1

                    print(
                        f"Cód: {partes[0]}, Título: {partes[1]}, Autor: {nome_autor}, Categoria: {nome_cat}, Status: {disponibilidade}")

            if opcao == '3':  # Ao final, mostrar a quantidade (REQUISITO 8)
                print("-" * 20)
                print(f"Total de Livros Disponíveis: {disponiveis}")
                print(f"Total de Livros Emprestados: {emprestados}")

        elif opcao == '4':
            cod = input("Digite o código do livro para excluir: ")
            # Muda o estado do livro (último campo) para '0'
            try:
                linhas_arquivo = open(arquivos_livros, "r", encoding='utf-8').readlines()
                encontrado = False
                for i, linha in enumerate(linhas_arquivo):
                    if linha.strip().split(';')[0] == cod:
                        partes = linha.strip().split(';')
                        partes[6] = "0"
                        linhas_arquivo[i] = ";".join(partes) + "\n"
                        encontrado = True
                        break
                if encontrado:
                    atualizar_arquivo(arquivos_livros, linhas_arquivo)
                    print("Livro excluído com sucesso.")
                else:
                    print("Livro não encontrado.")
            except FileNotFoundError:
                print("Arquivo de livros não existe.")

        elif opcao == '0':
            break


# REQUISITO 5) Ao incluir ou consultar dados na Tabela Empréstimos...
# REQUISITO 6) Permitir a realização da devolução do livro...
def gerenciar_emprestimos():
    global raiz_emprestimos
    global raiz_livros  # Precisamos para atualizar o status do livro
    while True:
        print("\n--- Menu Empréstimos e Devoluções ---")
        print("1. Realizar Empréstimo (Requisito 5)")
        print("2. Realizar Devolução (Requisito 6)")
        print("0. Voltar")
        opcao = input(">> Opção: ")

        if opcao == '1':
            cod_livro = input("Digite o código do livro: ")
            linha_livro = buscar_info_linha(arquivos_livros, cod_livro)

            if not linha_livro or linha_livro.split(';')[6] == '0':
                print("Erro: Livro não encontrado ou foi excluído.")
                continue

            # REQUISITO 5.1) Solicitar o código do livro e verificar na tabela Livros se o mesmo encontra-se disponível...
            partes_livro = linha_livro.split(';')
            if partes_livro[5] == '0':
                print("Erro: Livro já está emprestado.")
                continue

            # REQUISITO 5.2) Exibir o nome do livro e o nome da categoria.
            categoria_info = buscar_info_linha(arquivos_categorias, partes_livro[3])
            print(f"Livro a ser emprestado: {partes_livro[1]}")
            print(f"Categoria: {categoria_info.split(';')[1] if categoria_info else 'N/A'}")

            cod_aluno = input("Digite o código do aluno: ")
            linha_aluno = buscar_info_linha(arquivos_alunos, cod_aluno)
            if not linha_aluno or linha_aluno.split(';')[4] == '0':
                print("Erro: Aluno não encontrado ou foi excluído.")
                continue

            # REQUISITO 5.3) Buscar o código do aluno na tabela Alunos e exibir seu nome e o nome de sua cidade.
            cidade_info = buscar_info_linha(arquivo_cidades, linha_aluno.split(';')[3])
            print(f"Aluno: {linha_aluno.split(';')[1]}")
            print(f"Cidade: {cidade_info.split(';')[1] if cidade_info else 'N/A'}")

            confirmar = input("Confirmar empréstimo (s/n)? ").lower()
            if confirmar == 's':
                # REQUISITO 5.4) A data do empréstimo deverá ser a data do dia atual e a data de devolução deverá ser 7 dias além da data atual.
                hoje = date.today()
                devolucao = hoje + timedelta(days=7)
                cod_emprestimo = input("Digite um código para o novo empréstimo: ")

                # Formato: cod_emp;cod_livro;cod_aluno;data_emp;data_dev;devolvido(0=nao)
                linha_emp = f"{cod_emprestimo};{cod_livro};{cod_aluno};{hoje.strftime('%d/%m/%Y')};{devolucao.strftime('%d/%m/%Y')};0"
                adicionar_registro(arquivos_emprestimos, linha_emp)
                raiz_emprestimos = carregar_indices(arquivos_emprestimos)

                # REQUISITO 5.5) Após a confirmação do empréstimo, marcar a disponibilidade do livro como "emprestado"...
                try:
                    linhas_livros = open(arquivos_livros, "r", encoding='utf-8').readlines()
                    for i, linha in enumerate(linhas_livros):
                        if linha.strip().split(';')[0] == cod_livro:
                            partes = linha.strip().split(';')
                            partes[5] = "0"  # Muda disponibilidade para 0 (emprestado)
                            linhas_livros[i] = ";".join(partes) + "\n"
                            break
                    atualizar_arquivo(arquivos_livros, linhas_livros)
                except FileNotFoundError:
                    print("Arquivo de livros não encontrado para atualizar status.")

        elif opcao == '2':
            cod_emprestimo = input("Digite o código do empréstimo para devolução: ")
            linha_emp = buscar_info_linha(arquivos_emprestimos, cod_emprestimo)
            if not linha_emp:
                print("Erro: Empréstimo não encontrado.")
                continue

            partes_emp = linha_emp.split(';')
            cod_livro = partes_emp[1]
            data_devolucao_str = partes_emp[4]

            if partes_emp[5] == '1':
                print("Este livro já foi devolvido.")
                continue

            # REQUISITO 6.1) Verificar na tabela de empréstimos se o livro encontra-se dentro do prazo de devolução.
            data_devolucao = datetime.strptime(data_devolucao_str, "%d/%m/%Y").date()
            if date.today() > data_devolucao:
                print("Atenção: Devolução está ATRASADA!")

            confirmar = input("Confirmar devolução (s/n)? ").lower()
            if confirmar == 's':
                # REQUISITO 6.2) Após a confirmação da devolução, marcar a disponibilidade do livro como "disponível" e marcar o atributo devolvido como "Sim".
                try:
                    # Atualiza o empréstimo para "devolvido" (1)
                    linhas_emps = open(arquivos_emprestimos, "r", encoding='utf-8').readlines()
                    for i, linha in enumerate(linhas_emps):
                        if linha.strip().split(';')[0] == cod_emprestimo:
                            partes = linha.strip().split(';')
                            partes[5] = "1"  # Devolvido
                            linhas_emps[i] = ";".join(partes) + "\n"
                            break
                    atualizar_arquivo(arquivos_emprestimos, linhas_emps)

                    # Atualiza o livro para "disponível" (1)
                    linhas_livros = open(arquivos_livros, "r", encoding='utf-8').readlines()
                    for i, linha in enumerate(linhas_livros):
                        if linha.strip().split(';')[0] == cod_livro:
                            partes = linha.strip().split(';')
                            partes[5] = "1"  # Disponível
                            linhas_livros[i] = ";".join(partes) + "\n"
                            break
                    atualizar_arquivo(arquivos_livros, linhas_livros)
                    print("Devolução realizada com sucesso.")
                except FileNotFoundError:
                    print("Erro ao tentar ler arquivos para devolução.")

        elif opcao == '0':
            break


# REQUISITO 7) Permitir as seguintes consultas:
def menu_relatorios():
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Livros Emprestados Atualmente (Requisito 7.1)")
        print("2. Livros com Devolução Atrasada (Requisito 7.2)")
        print("3. Quantidade de Livros Emprestados por Período (Requisito 7.3)")
        print("0. Voltar")
        opcao = input(">> Opção: ")

        try:
            if opcao == '1' or opcao == '2':
                print("\n--- Relatório ---")
                with open(arquivos_emprestimos, "r", encoding='utf-8') as f_emp:
                    for linha_emp in f_emp:
                        partes_emp = linha_emp.strip().split(';')
                        # Pula se já foi devolvido
                        if partes_emp[5] == '1': continue

                        # Verifica se está atrasado
                        data_dev = datetime.strptime(partes_emp[4], "%d/%m/%Y").date()
                        atrasado = data_dev < date.today()

                        # Mostra se for o relatório 1, OU se for o relatório 2 e estiver atrasado
                        if (opcao == '1') or (opcao == '2' and atrasado):
                            livro_info = buscar_info_linha(arquivos_livros, partes_emp[1])
                            aluno_info = buscar_info_linha(arquivos_alunos, partes_emp[2])
                            titulo_livro = livro_info.split(';')[1] if livro_info else "N/A"
                            nome_aluno = aluno_info.split(';')[1] if aluno_info else "N/A"
                            print(f"Livro: {titulo_livro}, Aluno: {nome_aluno}, Devolver até: {partes_emp[4]}")

            elif opcao == '3':
                data_ini_str = input("Digite a data inicial (dd/mm/aaaa): ")
                data_fim_str = input("Digite a data final (dd/mm/aaaa): ")
                data_ini = datetime.strptime(data_ini_str, "%d/%m/%Y").date()
                data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y").date()

                contador = 0
                with open(arquivos_emprestimos, "r", encoding='utf-8') as f_emp:
                    for linha_emp in f_emp:
                        partes_emp = linha_emp.strip().split(';')
                        data_emp = datetime.strptime(partes_emp[3], "%d/%m/%Y").date()
                        # Verifica se a data do empréstimo está no período
                        if data_ini <= data_emp <= data_fim:
                            contador += 1
                print(f"\nForam emprestados {contador} livros entre {data_ini_str} e {data_fim_str}.")

            elif opcao == '0':
                break
            else:
                print("Opção inválida.")
        except FileNotFoundError:
            print("Arquivo de empréstimos não encontrado.")
        except ValueError:
            print("Formato de data inválido. Use dd/mm/aaaa.")


# --- Função Principal ---

def main():
    print("Iniciando o sistema da biblioteca...")

    global raiz_cidades, raiz_cursos, raiz_autores, raiz_categorias, raiz_alunos, raiz_livros, raiz_emprestimos

    # Carrega todos os índices no início
    raiz_cidades = carregar_indices(arquivo_cidades)
    raiz_cursos = carregar_indices(arquivos_cursos)
    raiz_autores = carregar_indices(arquivo_autores)
    raiz_categorias = carregar_indices(arquivos_categorias)
    raiz_alunos = carregar_indices(arquivos_alunos)
    raiz_livros = carregar_indices(arquivos_livros)
    raiz_emprestimos = carregar_indices(arquivos_emprestimos)

    while True:
        print("\n" + "=" * 10 + " MENU PRINCIPAL DA BIBLIOTECA " + "=" * 10)
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Livros")
        print("3. Gerenciar Cidades")
        print("4. Gerenciar Cursos")
        print("5. Gerenciar Autores")
        print("6. Gerenciar Categorias")
        print("7. Empréstimos e Devoluções")
        print("8. Relatórios")
        print("0. Sair do sistema")

        opcao = input(">> Escolha uma opção: ")

        match opcao:
            case '1':
                gerenciar_alunos()
            case '2':
                gerenciar_livros()
            case '3':
                gerenciar_cidades()
            case '4':
                gerenciar_cursos()
            case '5':
                gerenciar_autores()
            case '6':
                gerenciar_categorias()
            case '7':
                gerenciar_emprestimos()
            case '8':
                menu_relatorios()
            case '0':
                print("Encerrando o sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
# Esta linha especial garante que a função main() só vai rodar quando
# executamos este arquivo diretamente.
if __name__ == "__main__":
    main()