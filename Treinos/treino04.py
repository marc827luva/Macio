import random
sorteado=random.randint(1,100)
cont=0
while cont>-1:
    numero=int(input("Digite um número: "))
    if numero>sorteado:
        print("Abaixo")
        cont+=1
    elif numero<sorteado:
        print("Acima")
        cont+=1
    elif numero==sorteado:
        cont+=1
        print("Parabéns vc acertou o numero com tentativas",cont)
        cont=-5
print("Fim do Programa")