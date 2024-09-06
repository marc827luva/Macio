import random

# Listas para cada letra da palavra BINGO
B = list(range(1, 16))
I = list(range(16, 31))
N = list(range(31, 46))
G = list(range(46, 61))
O = list(range(61, 76))

# Dicionário para armazenar as listas associadas às letras
bingo_lists = {
    'B': B,
    'I': I,
    'N': N,
    'G': G,
    'O': O
}

# Função para sortear um valor de uma lista
def sortear_valor():
    letra = random.choice(list(bingo_lists.keys()))
    lista = bingo_lists[letra]
    
    if lista:
        valor = random.choice(lista)
        lista.remove(valor)
        return letra, valor
    else:
        # Caso a lista esteja vazia, tenta sortear de uma nova lista
        return sortear_valor()

def main():
    print("Bem-vindo ao sistema de Bingo!")
    
    while True:
        letra, valor = sortear_valor()
        print(f"Letra: {letra}, Valor: {valor}")
        
        # Pergunta ao usuário se deseja um novo sorteio
        resposta = input("Deseja um novo sorteio? (s/n): ").strip().lower()
        if resposta != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()
