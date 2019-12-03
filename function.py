# Wystepuja 2 rodzaje funkcji.
# tworzymy za pomoca przedrostka def nazwa()

def nazwa():
    pass

# Twierdzenie Pitagorasa
# def pit(a,b):
#     c = (a**2 + b**2)**.5
#     return c

# przeciwprostokatna = pit(3,4)
# print(przeciwprostokatna)

#srednia arytmetyczna
def arytm(list):
    suma = 0
    for i in list:
        suma += i
    srednia = suma / len(list)
    return srednia
lista = [1,2,3,4,5]
print(arytm(lista))
print('---'*10)

#funckja wyszukujaca pierw. funkcji kwadratowej (1,-4,3, [1,3])
import math
def funkcjaKwadratowa(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (math.sqrt(delta) - b)/2*a
        x2 = (- math.sqrt(delta) - b)/2*a
        return x1, x2
    elif delta == 0:
        x = -b/2*a
        return x
    else:
        print('Funkcja nie posiada miejsc zerowych.')

print(funkcjaKwadratowa(1,-4,3))
print('---'*10)

#zaimplementowana silnia rekurencyjnie

def silnia_iteracyjna(x):
    factorial = 1
    if x > 0:
        for i in range(1, x+1):
            factorial *= i
        return factorial
    else:
        print('Podaj liczbe wieksza od 0')
        
print(silnia_iteracyjna(5))
print('---'*5)

def silnia_rekurencyjna(x):
    if x == 1:
        return 1
    else:
        return silnia_rekurencyjna(x-1) * x
print(silnia_rekurencyjna(5))
print('---'*5)
print(silnia_rekurencyjna(7))
print('---'*10)