# element mapujacy/haszujacy/ funckja skrotu -> wikipedia
# do slownikow nie wsadzimy elementow mutowalnych

# dictionary
# dict()

# lista jako klucz nie, 
slownik = {
    'klucz': [2,4,5],
    (1,2,3): 'wartosc2',
    'd': 'wartosc3',
    (0,4): 'X',
    True: 'tak',
    'tal': False,
    #(1,3, [2,4,5]): '234,'
    None: 'sf'

}
print(slownik)

#dodawanie elementu do slownika
slownik['kolejnyKlucz'] = 'AAAAAA'
print(slownik)

#zmiana elementu tak samo
slownik['kolejnyKlucz'] = 'BBB'
print(slownik)

#usuwanie elementu
del slownik['kolejnyKlucz']
print(slownik)

# sprawdzanie czy element znajduje sie w slowniku
print('a' in slownik)