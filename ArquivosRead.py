import os


def leArquivo(n):
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual,
                   "Dados", f"DadosLista_{n}.txt"), "r")
    numeros = []

    for linha in arquivo:
        numero = linha.strip()
        numeros.append(int(numero))

    arquivo.close()
    return numeros


def leArquivoTimeSequencial(n):
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "Dados",
                   f"DadosTimeSequencial_{n}.txt"), "r")
    numeros = []

    for linha in arquivo:
        numero = linha.strip()
        numeros.append(float(numero))

    arquivo.close()
    return numeros


def leArquivoBusca(n):
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "Dados",
                   f"DadosListaBusca_{n}.txt"), "r")
    numeros = []

    for linha in arquivo:
        numero = linha.strip()
        numeros.append(int(numero))

    arquivo.close()
    return numeros
