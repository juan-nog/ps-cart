# Programa 2

def enunciado():
    """
    Joãozinho te propôs o seguinte desafio: ele escolheu dois inteiros A e B, com 1 ≤ A ≤ B ≤ 101000, 
    e escreveu na lousa todos os inteiros entre A e B, em sequência, porém colocando um espaço após 
    cada dígito, de forma a não ser possível ver quando um número termina ou começa. Por exemplo, se 
    Joãozinho escolher A = 98 e B = 102, ele escreveria a sequência “9 8 9 9 1 0 0 1 0 1 1 0 2”. 
    Seu desafio é: dada a lista de dígitos escritos na lousa, encontrar os valores de A e B. 
    Caso exista mais de uma possibilidade para os valores que geraria a lista, você deve encontrar uma em que 
    o valor de A é o menor possível. É garantido que a lista de dígitos da lousa tem no máximo tamanho 1000.

    Entrada

    A primeira linha da entrada contém um único inteiro N, indicando o número de dígitos. 
    A segunda linha contém N inteiros di, indicando os dígitos escritos.

    Saída

    Imprima o menor valor possível de A. 
    Restrições 
    • 1 ≤ N ≤ 1000 
    • 0 ≤ di ≤ 9 
    
    Informações sobre a pontuação 
    • Para um conjunto de casos de testes valendo 21 pontos, 1000 ≤ A ≤ B ≤ 9999. 
    • Para outro conjunto de casos de testes valendo 23 pontos, B = A + 1. 
    • Para outro conjunto de casos de testes valendo 40 pontos, A, B < 106 . 
    • Para outro conjunto de casos de testes valendo 16 pontos, nenhuma restrição adicional.

    Exemplo de entrada
    6 1 2 3 1 2 4

    Exemplo de saída
    123
    """

def find_A(digits_string):

    digits_string = digits_string.replace(' ', '')

    # Let q be the number of digits of A. Since A < 101000, we test q up to 6.
    for q in range(1, 7): 
        A_try = int(digits_string[:q])

        # Following loops tests if A_try is the first of a sequence of consecutive integers in digits_string
        # set variables before start the loop
        next = A_try # integer value of the sequence
        start_try = str(A_try) # substring that digits_string starts with

        while len(start_try) < len(digits_string):
            next = next + 1
            start_try = str(start_try) + str(next)
            if start_try == digits_string[:len(start_try)]: 
                continue
            else: break
        if start_try == digits_string: return A_try
        else: continue # jump to next q
    
    # if it gets this far, it couldn't find the right A
    print("No A value found.")
    return None

def testes():
    print(find_A("1 2 3 1 2 4"))
    print(find_A("1 2 3 1 2 4") == 123)
    print(find_A("9 8 9 9 1 0 0 1 0 1 1 0 2") == 98)
    print(find_A("14") == 14)
    print(find_A("1458145914601461") == 1458)

def teste_humano():
    while True:
        digits_input = input("\nInsira a sequência: ")
        print('Resposta:', find_A(digits_input))

def main():
    n = int(input("Insira o número de dígitos da sequência: ")) # this value isn't actually used
    digits_input = input("Insira a sequência: ")
    print(find_A(digits_input))

# testes()

# teste_humano()

main()