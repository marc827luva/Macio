import random
a=int(input("Digite 0 para rodar um dado ou 1 para sair: "))
while a==0:
    dado=random.randint(1,6)
    print("O numero sorteado foi",dado)
    a=int(input("Digite 0 para rodar um dado ou 1 para sair: "))
print("Fim de jogo")