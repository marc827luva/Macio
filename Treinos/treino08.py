numeroGi=int(input("digie a quatidade de numeros que desejs na lista: "))
listaNumeros=[]
while numeroGi > 0:
    numeros0riginais=int(input("digite um número :"))
    if numeros0riginais%2 == 0:
        listaNumeros.append(numeros0riginais*2)
    elif numeros0riginais%2 == 1:
        listaNumeros.append(numeros0riginais*3-1)
    numeroGi -= 1
print(listaNumeros)