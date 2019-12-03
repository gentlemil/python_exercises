# algorytm sito-erastotenesa
lista = []
newLista = []


for i in range(1,101):
    lista.append(i)

for i in lista:
    for j in range(2,10):
        if (i % j == 0):
            newLista.append(i)
            list(set(newLista))

print('------'*10)
print(list(set(lista) - set(newLista)))
print('------'*10)

# for i in lista:
#     if(i % 2 == 0):
#         lista.remove(i)
# for i in lista:
#     if(i % 3 == 0):
#         lista.remove(i)    
# for i in lista:
#     if(i % 4 == 0):
#         lista.remove(i)    
# for i in lista:
#     if(i % 5 == 0):
#         lista.remove(i)    
# for i in lista:
#     if(i % 6 == 0):
#         lista.remove(i)    
# for i in lista:
#     if(i % 7 == 0):
#         lista.remove(i)    
# for i in lista:
#     if(i % 8 == 0):
#         lista.remove(i)    
# for i in lista:
#     if(i % 9 == 0):
#         lista.remove(i)
# print(lista)        