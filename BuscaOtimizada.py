import time
import AlgoritmoOrdenacao as AO

# Busca Sequencial Otimizada


def buscaSequencialOtimizada(V, q):
    inicio = time.time()
    n = len(V)
    m = len(q)
    arquivo = open(f"DadosEncontrados_{m}_{n}.txt", "w")
    VOrdenado = AO.heapsort(V)
    print("Busca Vetor Otimizado: ", len(V))
    for i in range(len(q)):
        # print("Busca Otimizado: ", i)
        for j in range(len(VOrdenado)):
            if VOrdenado[j] <= q[i]:
                if VOrdenado[j] == q[i]:
                    arquivo.write(str(q[i]) + "\n")
            else:
                break
    fim = time.time()
    BuscaSequencialOtimizada = fim - inicio
    arquivo.close()
    return BuscaSequencialOtimizada
