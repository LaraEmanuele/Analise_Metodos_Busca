def gerarArquivoDadosEncontrados(n, m):
    # n = tamanho da lista de numeros
    # m = quantidade de numeros buscados
    with open(f"DadosEncontrados_{m}_{n}.txt", "w") as arquivo:
        arquivo = ""
