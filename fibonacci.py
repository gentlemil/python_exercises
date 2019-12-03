lista = [0,1]
for i in range(0, 10):
    lista[i] = lista[i-1] + lista[i-2]
    lista.append(lista[i])
print(lista[-1])