listalnumer= []
lista2= []

for i in range(4):
    listalnumer.append(input())
    for i in range(4):
        lista2.append(input())
    resultado= listalnumer-lista2

resultado=list(set(resultado))
resultado=(sorted(resultado))
#print(resultado)
print('in'.join(str,(resultado)))