import time
import AlgoritmoOrdenacao as AO


def pesquisaBinariaElementoUnico(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. O elemento não está presente.
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. O elemento está no meio do arranjo.
    if A[meio] == item:
        return meio
    # 3. Atualizamos os limites e continuamos a busca.
    elif A[meio] > item:
        return pesquisaBinariaElementoUnico(A, esquerda, meio - 1, item)
    else:  # A[meio] < item
        return pesquisaBinariaElementoUnico(A, meio + 1, direita, item)

# Busca Binária


def buscaBinariaLista(V, q, esquerda, direita):
    inicio = time.time()
    result = []
    VOrdenado = AO.heapsort(V)
    print("Busca Vetor Binario: ", len(V))
    for i in range(len(q)):
        # print("Busca Binario: ", i)
        indice = pesquisaBinariaElementoUnico(
            VOrdenado, esquerda, direita, q[i])
        if indice != -1:
            result.append(str(VOrdenado[indice]))
    fim = time.time()
    BuscaBinaria = fim - inicio
    return BuscaBinaria
