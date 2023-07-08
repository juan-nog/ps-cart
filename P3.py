# Problema 3

def enunciado():
    '''
    Um quadrado fantástico é um conjunto de números inteiros positivos dispostos 
    em N linhas por N colunas, tal que: 
    • Não há números repetidos no quadrado. 
    • A média dos números em cada linha é um número inteiro que está presente na linha. 
    • A média dos números em cada coluna é um número inteiro que está presente na coluna.

    Entrada

    A primeira e única linha da entrada contém um número inteiro N, indicando a dimensão do quadrado.

    Saída

    Seu programa deve produzir N linhas, cada uma contendo N números inteiros Xi , 
    representando um quadrado fantástico.

    Restrições 
    • 1 ≤ N ≤ 40 
    • 1 ≤ Xi ≤ 1000000

    Informações sobre a pontuação 
    • Para um conjunto de casos de testes valendo 44 pontos, 1 ≤ N é ímpar. 
    • Para outro conjunto de casos de testes valendo 56 pontos, nenhuma restrição adicional.

    Exemplo de entrada
    1

    Exemplo de saída
    1
    '''

def matrix_odd_case(n):
    """Prints a matrix that solves the question for odd dimensions. Input n: dimension of the matrix."""

    p = 10000
    a = 1 # horizontal jump in adjacent elements
    b = 100 # vertical jump in adjacent elements

    v = int(- (n - 1)/ 2)

    for i in range(n): # line i
        
        h = int(- (n - 1)/ 2)

        for j in range(n): # column j
            print(p + (v * b) + (h * a), end='\t')
            h += 1
        print() # line break
        v += 1
    
def matrix_even_case(n):
    """Prints a matrix that solves the question for even dimensions. Input n: dimension of the matrix."""

    p = 10000
    a = 1 # horizontal jump in adjacent elements, except in the middle of the line 
    b = 100 # vertical jump in adjacent elements, except in the middle of the column

    # if n == 4: v = -2
    # else: 
    v = int(- (n / 2) - 1)

    for i in range(n): # line i
        if v == -3: v = -2
        elif v == 1: v = 3
        
        # if n == 4: h = -2
        # else: 
        h = int(- (n / 2) - 1)

        for j in range(n): # column j
            if h == -3: h = -2
            elif h == 1: h = 3
            print(p + (v * b) + (h * a), end='\t')
            h += 1
        print() # line break
        v += 1

def main():
    N = int(input("Indique a dimensão do quadrado: "))
    if N > 40: print("Não se deve utilizar dimensão N > 40.")
    elif N == 2: print("Não é possível gerar um quadrado fantástico 2x2.")
    elif N % 2 == 0: matrix_even_case(N)
    elif N % 2 == 1: matrix_odd_case(N)

def teste():
    while True: 
        main()
        print()

teste()