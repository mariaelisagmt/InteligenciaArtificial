from random import *
import random

def funcao_transicao(estado_inicial, posicao):
    estado_inicial[posicao] = 'l'
    print (f"Limpando a Sala {estado_inicial[0]}")
    return estado_inicial

def acoes(estado_inicial, estado_objetivo):
    x = 0
    estado = []
    for x in range(1,5):
        if(estado_inicial[x] != estado_objetivo[x]):
            estado = funcao_transicao(estado_inicial, x)
    return estado
    
def main():
    #Estado Inicial do Problema
    estado_inicial_A = ['A', random.choice(['s', 'l']),
                             random.choice(['s', 'l']),
                             random.choice(['s', 'l']),
                             random.choice(['s', 'l'])
                        ]
    estado_inicial_B = ['B', random.choice(['s', 'l']),
                              random.choice(['s', 'l']),
                              random.choice(['s', 'l']),
                              random.choice(['s', 'l'])
                        ]
    print ("Estado Inicial da Sala A: ", estado_inicial_A)
    print ("Estado Inicial da Sala B: ", estado_inicial_B)
    print ("Estado Objetivo: Sala A e B Limpas! ")
    #Estado Objeto do Problema
    estado_objetivo_A = ['A', 'l','l','l','l']
    estado_objetivo_B = ['B', 'l','l','l','l']
    #print(f'Estado Inicial = {estado_inicial} Estado Final = {estado_objetivo}')

    while (True):
        if (estado_inicial_A != estado_objetivo_A):
            estado_inicial_A = acoes(estado_inicial_A, estado_objetivo_A)
        else:
            if (estado_inicial_B != estado_objetivo_B):
                estado_inicial_B = acoes(estado_inicial_B, estado_objetivo_B)
            else:
                print("Objetivo Final Alcançado! Sala A e B limpa!")
                break
            


if __name__ == '__main__':
    main()