import time

# Busca Sequencial


def buscaSequencial(V, q):
    inicio = time.time()  # Salva o tempo de inicio
    n = len(q)
    result = []
    print("Busca Sequencial Vetor: ", len(V))
    for i in range(len(q)):
        # print("Busca Sequencial: ", i)
        for j in range(len(V)):
            if V[j] == q[i]:
                result.append(str(q[i]))
    fim = time.time()  # Salva o tempo de fim
    BuscaSequencial = fim - inicio  # Calcula o tempo de execução
    return BuscaSequencial
