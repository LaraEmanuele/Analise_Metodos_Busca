import os
import BuscaSequencial as BS
import BuscaOtimizada as BO
import BuscaBinaria as BB


def calculaTempoExecucao(n1, n2, n3, n4, m):
    # n = tamanho da lista de numeros
    # m = quantidade de numeros buscados

    # Busca Sequencial
    diretorio_atual = os.getcwd()
    with open(os.path.join(diretorio_atual, "Dados", f"DadosListaBusca_{len(m)}.txt"), "w") as arquivo:
        # Busca 10^4
        arquivo.write(str(BS.buscaSequencial(n1, m)) + "\n")

        # Busca 10^5
        arquivo.write(str(BS.buscaSequencial(n2, m)) + "\n")

        # Busca 10^6
        arquivo.write(str(BS.buscaSequencial(n3, m)) + "\n")

        # Busca 10^7
        arquivo.write(str(BS.buscaSequencial(n4, m)) + "\n")

    # Busca Otimizada
    with open(os.path.join(diretorio_atual, "Dados", f"DadosTimeOtimizada_{len(m)}.txt"), "w") as arquivo:
        # Busca 10^4
        arquivo.write(str(BO.buscaSequencialOtimizada(n1, m)) + "\n")

        # Busca 10^5
        arquivo.write(str(BO.buscaSequencialOtimizada(n2, m)) + "\n")

        # Busca 10^6
        arquivo.write(str(BO.buscaSequencialOtimizada(n3, m)) + "\n")

        # Busca 10^7
        arquivo.write(str(BO.buscaSequencialOtimizada(n4, m)) + "\n")

    # Busca Binária
    with open(os.path.join(diretorio_atual, "Dados", f"DadosTimeBinaria_{len(m)}.txt"), "w") as arquivo:
        # Busca 10^4
        arquivo.write(str(BB.buscaBinariaLista(n1, m, 0, len(n1) - 1)) + "\n")

        # Busca 10^5
        arquivo.write(str(BB.buscaBinariaLista(n2, m, 0, len(n2) - 1)) + "\n")

        # Busca 10^6
        arquivo.write(str(BB.buscaBinariaLista(n3, m, 0, len(n3) - 1)) + "\n")

        # Busca 10^7
        arquivo.write(str(BB.buscaBinariaLista(n4, m, 0, len(n4) - 1)) + "\n")

    return
