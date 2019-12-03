# set
# nie moga sie powtarzac elementy, jest mutowalny
# frozenset jest niemutowalny
# nie dodamy listy, slownika

zbior = {'a', 'b', 1,2,5, 'C'}
innyZbior = {'b', 1, 5, 'D', 'X', 3}

#operacje matematyczne na zbiorach
print(zbior.isdisjoint(innyZbior)) #zbiory nie maja el. wspolnych
print(zbior < innyZbior) # .issubset(innyZbior)
print(zbior <= innyZbior) # lekki warunek
print(zbior > innyZbior) # .issuperset(innyZbior) mocny warunek, nadzbior
print(zbior >= innyZbior) # lekki warunek
print(zbior == innyZbior) # czy sa identyczne
print(zbior | innyZbior) # suma zbiorow
print(zbior & innyZbior) # iloczyn zbiorow (tylko el. wspolne)
print(zbior - innyZbior) # roznica zbiorow
print(zbior ^ innyZbior) # symetryczna roznica zbiorow