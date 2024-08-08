cont=1
while cont==1:
    palavra=input("Digite uma palavra: ")
    for numeros,letras in enumerate(palavra):
        print(numeros+1, '- ' ,letras)
    cont=int(input("Digite 1 para Jogar novamente e 0 para sair: "))
print("Fim de jogo")