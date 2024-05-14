import random
import time
import os

class Tiporeg:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2

class No:
    def __init__(self, registro):
        self.registro = registro
        self.esquerda = None
        self.direita = None

def novoNo(pRegistro):
    no = No(pRegistro)
    no.esquerda = None
    no.direita = None
    return no

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.numero_interacoes = 0

    def inserir(self, no, registro):
        if no is None:
            return novoNo(registro)

        if registro.chave < no.registro.chave:
            no.esquerda = self.inserir(no.esquerda, registro)
        elif registro.chave > no.registro.chave:
            no.direita = self.inserir(no.direita, registro)

        return no

    def Buscar(self, no, chave):
        if no is None:
            return False

        if chave < no.registro.chave:
            self.numero_interacoes += 1
            return self.Buscar(no.esquerda, chave)
        elif chave > no.registro.chave:
            self.numero_interacoes += 1
            return self.Buscar(no.direita, chave)
        else:
            return True

def retornaTipoReg(s):
    aux = Tiporeg(0, 0, "")
    auxS = s
    delimiter = ";"
    pos = s.find(delimiter)
    aux.chave = int(s[:pos])
    aux.dado1 = int(s[pos + 1:])
    pos = s.find(delimiter, pos + 1)
    auxS = s[pos + 1:]
    aux.dado2 = auxS
    return aux

# Inicializa o gerador de números aleatórios com uma semente baseada no tempo atual
random.seed(time.time())

# Cria uma instância da estrutura ArvoreBinaria
arv = ArvoreBinaria()

# Variáveis para leitura do arquivo e controle
nomeArquivo = "dadosOrdenados10000.txt"
totalPresente = 1
totalAusente = 1
vetorEncontradas = ["" for _ in range(16)]
vetorNaoEncontradas = ["" for _ in range(16)]

# Inicializa a raiz da árvore como nula
arv.raiz = None

# para especificar o nome do arquivo que vai ser aberto
arquivo = open("Arquivos Entrada/" + nomeArquivo, "r")

# Verifica se o arquivo foi aberto corretamente
if not arquivo:
    print("Erro ao abrir o arquivo.")
    exit(1)

# Lê dados do arquivo e insere na árvore binária de busca
for linha in arquivo:
    if linha.strip() != "":
        auxiliar = retornaTipoReg(linha.strip())
        arv.raiz = arv.inserir(arv.raiz, auxiliar)

# Fecha o arquivo após a leitura
arquivo.close()

# Realiza operações de busca aleatória na árvore binária
gerouTodas = False
while not gerouTodas:
    if totalAusente < 15:
        chaveAleatoria = random.randint(0, 19999)
    else:
        chaveAleatoria = random.randint(0, 9999)

    arv.numero_interacoes = 0
    start_time = time.time()

    resultadoChaveEncontrada = arv.Buscar(arv.raiz, chaveAleatoria)

    end_time = time.time()
    elapsed_time = end_time - start_time

    if resultadoChaveEncontrada:
        if totalPresente <= 15:
            vetorEncontradas[totalPresente - 1] = f"Chave ({chaveAleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}"
            totalPresente += 1
    else:
        if totalAusente <= 15:
            vetorNaoEncontradas[totalAusente - 1] = f"Chave ({chaveAleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}"
            totalAusente += 1

    gerouTodas = totalAusente == 16 and totalPresente == 16

# Abre o arquivo de saída "arquivo_saida.txt"
arquivo_saida = open(f"Arquivos Saida/binaria/arquivo_saida_{nomeArquivo}", "w")

# Verifica se o arquivo de saída foi aberto corretamente
if not arquivo_saida:
    print("Erro ao abrir o arquivo de saída.")
    exit(1)

# Escreve as chaves encontradas no arquivo de saída
for i in range(15):
    arquivo_saida.write(vetorEncontradas[i] + "\n")

# Escreve as chaves não encontradas no arquivo de saída
for i in range(15):
    arquivo_saida.write(vetorNaoEncontradas[i] + "\n")

# Fecha o arquivo de saída
arquivo_saida.close()
