lotek = []
while len(lotek) < 6:
    # counter += 1

    nr = int(input('Podaj liczbe: '))
    if nr in lotek:
        print('dupa')
        break
    else:
        lotek.append(nr)
        continue

print(lotek)

# II SPOSOB
# lotek = []
# while len(lotek) <6:
#     liczba = int(input('podaj liczbe'))

#     if not (1<=loczba<=49):
#         print('nie oszukuj!')
#         break

#     if liczba not in lotek:
#         lotek.append(liczba)

# print('wylosowane liczby to: ', lotek)