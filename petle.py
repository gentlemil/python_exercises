lista = ['a', 'b', 'c', 'p']
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print("-"*16)
# Wyrozniamy 2 rodzaje petli w Pythonie: 'for' oraz 'while'
for word in lista:
    print(word)

print("-"*16)
# ----------------------

lista2 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for number in lista2:
    print(number, end=' ')

print("-"*16)
# ----------------------

lista2 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for number in lista2:
    print(number, number**2, number**(0.5), sep='\t',)

print("-"*16)
# ----------------------

imie = "Milosz"
# imie.upper()    #PIOTR
for letter in imie:
    print(letter.upper())

print("-"*16)
# ----------------------

slownik = {
    1: "Beata",
    2: "Milosz",
    3: "Marek",
    4: "Marcin",
    5: "Lukasz"
}

for key, value in slownik.items():
    print(key, value)
    
print("-"*16)
# ----------------------

lista3 = ['Milosz', 'Beata', 'Marek', 'Marcin', 'Lukasz']
for imie in lista3:
    print(imie)

print("-"*16)
# --- albo --------
for miejsce, imie in enumerate(lista3):
    print(miejsce, imie)
print("-"*16)

lista4 = [
    ('a', '1'),
    ('b', '2'),
]
for literka, cyferka in lista4:
    print(literka, cyferka)
print("-"*16)
# ----------------------

for i in range(2,21,2):
    print(i)

print("-"*16)    
# ----------------------

# /3 -> fizz

for i in range(1,101):
    if (i % 3 == 0 and i % 5 != 0):
        print(i, ' fizz')
    elif (i % 5 == 0 and i % 3 != 0):
        print(i, ' buzz')
    elif (i % 15 == 0):
        print(i, ' FizzBuzz')

print("-"*16)    
# ----------------------
if "Piotr" in "Piotr Banaszkiewicz":
    print('sieeeema')

print("-"*16)    
# ----------------------






# print("-"*16)    
# ----------------------
# print("-"*16)    
# ----------------------