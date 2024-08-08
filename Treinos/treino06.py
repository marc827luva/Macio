cont=1
while cont==1:
    nome=[]
    nome.append(input("Digite um nome: "))
    if nome[0]=="":
        cont=0
    else:
        a=nome[0]
        print("Esse nome tem", len(a) , "letras.")
print("Fim do Programa")