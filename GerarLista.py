# Gerador de lista de números aleatórios com tamanho n
import random


def gerarLista(n):
    numeros = set()
    count = 0
    with open(f"DadosLista_{n}.txt", "w") as arquivo:
        while count < n:
            numeroAleatorio = random.randint(0, (10*n))
            if numeroAleatorio not in numeros:
                arquivo.write(str(numeroAleatorio) + "\n")
                numeros.add(numeroAleatorio)
                count += 1


def gerarListaBusca(n, rangeAleatorio):
    numeros = set()
    count = 0
    with open(f"DadosListaBusca_{n}.txt", "w") as arquivo:
        while count < n:
            numeroAleatorio = random.randint(0, (10*rangeAleatorio))
            if numeroAleatorio not in numeros:
                arquivo.write(str(numeroAleatorio) + "\n")
                numeros.add(numeroAleatorio)
                count += 1
