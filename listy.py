# list() []
zmienna = 'tekst'
lista = [ 
    True,
    False,
    None,
    -1,
    3.14,
    5+6j,
    "Piotr",
    [],
    zmienna,
]
print(lista)
print(lista[0])
print(lista[3:])    #wyswietlanie od trzeciego elementu
print(lista[5])
print(len(lista))   #zwraca liczba elementow tablicy
print(lista[-1])

lista.append(0) # append - dodawanie elementu na koncu listy
lista.insert(5, 'dupa')  # insert - wstawienia do liczby w konkretnym miejscu
lista[2] = 12  # wstawianie w konkretnym miejscu zamieniajac to co tam bylo wczesniej
# elementy w liscie mozna zmienic, ALE stringa juz NIE!
print(lista)
del lista[4]
print(lista)

