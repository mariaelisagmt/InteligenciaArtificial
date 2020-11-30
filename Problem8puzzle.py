import Biblioteca8puzzle as dll
from random import *
import time

#Cria Tabuleiro
def cria_tabuleiro(items):
    #Setando um dicionário
    tabuleiro = {}
    tabuleiro["pecas"] = [[items[i * 3 + j] for j in range(3)] for i in range(3)]

    #Verifica peca "branca"
    for i in range(3):
        for j in range(3):
            if (tabuleiro["pecas"][i][j] == 0):
                tabuleiro["posicao"] = i, j
                break
    return tabuleiro

#Movimentando peças para esquerda
def mover_esquerda(tabuleiro):
    #Posicao Atual [i, j]
    i, j = tabuleiro["posicao"]

    #Impossibilidade de movimento
    if j == 0: return None

    novo = {}
    novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
    novo["pecas"][i][j], novo["pecas"][i][j - 1] = novo["pecas"][i][j - 1], novo["pecas"][i][j]
    novo["posicao"] = i, j - 1

    return novo

#Movimentando peças para direita
def mover_direita(tabuleiro):
    #Posicao Atual [i,j]
	i, j = tabuleiro["posicao"] 

    #Impossibilidade de movimento
	if j == 2: return None

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i][j + 1] = novo["pecas"][i][j + 1], novo["pecas"][i][j]
	novo["posicao"] = i, j + 1

	return novo

#Movimentando peças para cima
def mover_cima(tabuleiro):
    #Posicao Atual [i,j]
	i, j = tabuleiro["posicao"]

    #Impossibilidade de movimento
	if i == 0: return None

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i - 1][j] = novo["pecas"][i - 1][j], novo["pecas"][i][j]
	novo["posicao"] = i - 1, j

	return novo

#Movimentando peças para cima
def mover_baixo(tabuleiro):
    #Posicao Atual [i,j]
	i, j = tabuleiro["posicao"]

    #Impossibilidade de movimento
	if i == 2: return None

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i + 1][j] = novo["pecas"][i + 1][j], novo["pecas"][i][j]
	novo["posicao"] = i + 1, j

	return novo

#Funcao de custo
def funcao_custo(tabuleiro):
	return 1

def verifica_objetivo(tabuleiro):
	return tabuleiro["pecas"] == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def enfileira_lifo(lista_1,lista_2):
	return lista_1 + lista_2

#Implementação da Distancia de Manhattan
def heuristica_manhattan(tabuleiro):
	meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
	soma = 0
	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					if meta[i][j] == tabuleiro["pecas"][k][l]:
						soma = soma + abs(int(i - k)) + abs(int(j - l))
	return soma

#Implementação da Quantidade de Peças fora do Lugar
def heuristica_desordenado(tabuleiro):
    meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    contador = 0
    for i in range(3):
        for j in range(3):
            if meta[i][j] != tabuleiro["pecas"][i][j]:
                contador = contador + 1
    return contador

def main():
    #Peças do Tabuleiro
	items = [7,2,4,5,0,6,8,3,1]
    #Criando o Tabuleiro
	tabuleiro = cria_tabuleiro(items)
    #Ações Possíveis:
	operadores = [mover_baixo, mover_cima, mover_direita, mover_esquerda]

	#Distância de Manhattan
	problema_manhattan = dll.Problema(tabuleiro, operadores, verifica_objetivo, heuristica_manhattan)

	inicio_manhattan = time.time()
	resultado_problema_manhattan = dll.buscaaestrela(problema_manhattan, enfileira_lifo)
	fim_manhattan = time.time()

    #Quantidade de peças fora do lugar
	problema_desordenado = dll.Problema(tabuleiro, operadores, verifica_objetivo, heuristica_desordenado)

	inicio_desordenado = time.time()
	resultado_problema_desordenado = dll.buscaaestrela(problema_desordenado, enfileira_lifo)
	fim_desordenado = time.time()
    

	print ("Problema do Quebra Cabeça de 8 Pecas")
	print ("-------------------------------------------------")
	print ("H1 - Peças fora do lugar")
	print ("Estado Inicial:",tabuleiro["pecas"])
	print ("Saida Busca A*: ", resultado_problema_desordenado)
	print ("Tempo: ", fim_desordenado - inicio_desordenado)
	print ("Número de comparacoes: ", problema_desordenado.comparacoes)
	print ("-------------------------------------------------")
	print ("H2 - Distância de Manhattan")   
	print ("Estado Inicial:",tabuleiro["pecas"])
	print ("Saida Busca A*: ", resultado_problema_manhattan)
	print ("Tempo: ", fim_manhattan - inicio_manhattan)
	print ("Número de comparacoes: ", problema_manhattan.comparacoes)
	print ("-------------------------------------------------")

	return 0

if __name__ == "__main__":
    main()