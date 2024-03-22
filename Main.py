# Bibliotecas
import ArquivosRead as AR
import BuscaSequencial as BS
import BuscaOtimizada as BO
import BuscaBinaria as BB
import GerarLista as GL
import CalculoTempo as CT
import ListaElementosChavesEncontrados as LECE

"""
#Código utlizado para gerar as listas
GL.gerarLista(10000)
GL.gerarLista(100000)
GL.gerarLista(1000000)
GL.gerarLista(10000000)


#Gerar listas de elementos chaves
GL.gerarListaBusca (100, 10000)
GL.gerarListaBusca (1000, 100000)
GL.gerarListaBusca (10000, 1000000)
GL.gerarListaBusca (100000, 10000000)


#Gera os arquivos para armazenar os indices e valores que coinciedem entre as listas
LECE.gerarArquivoDadosEncontrados (10000, 100)
LECE.gerarArquivoDadosEncontrados (100000, 100)
LECE.gerarArquivoDadosEncontrados (1000000, 100)
LECE.gerarArquivoDadosEncontrados (10000000, 100)

LECE.gerarArquivoDadosEncontrados (10000, 1000)
LECE.gerarArquivoDadosEncontrados (100000, 1000)
LECE.gerarArquivoDadosEncontrados (1000000, 1000)
LECE.gerarArquivoDadosEncontrados (10000000, 1000)


LECE.gerarArquivoDadosEncontrados (10000, 1000)
LECE.gerarArquivoDadosEncontrados (100000, 1000)
LECE.gerarArquivoDadosEncontrados (1000000, 1000)
LECE.gerarArquivoDadosEncontrados (10000000, 1000)

LECE.gerarArquivoDadosEncontrados (10000, 10000)
LECE.gerarArquivoDadosEncontrados (100000, 10000)
LECE.gerarArquivoDadosEncontrados (1000000, 10000)
LECE.gerarArquivoDadosEncontrados (10000000, 10000)
"""


# Leitura dos arquivos
# Obtenção das listas com 10^4
V10000 = AR.leArquivo(10000)
B100 = AR.leArquivoBusca(100)


# Obtenção das listas com 10^5
V100000 = AR.leArquivo(100000)
B1000 = AR.leArquivoBusca(1000)

# Obtenção das listas com 10^6
V1000000 = AR.leArquivo(1000000)
B10000 = AR.leArquivoBusca(10000)

# Obtenção das listas com 10^7
V10000000 = AR.leArquivo(10000000)
B100000 = AR.leArquivoBusca(100000)

CT.calculaTempoExecucao(V10000, V100000, V1000000, V10000000, B100)

CT.calculaTempoExecucao(V10000, V100000, V1000000, V10000000, B1000)

CT.calculaTempoExecucao(V10000, V100000, V1000000, V10000000, B10000)

CT.calculaTempoExecucao(V10000, V100000, V1000000, V10000000, B100000)
