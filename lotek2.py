# 5x odczytac liczbe od uzytkownika i dopisac ja do listy
# wylosowanych liczb
lotek = []
for nr in range(0,6):
    nrr = int(input("Podaj liczbe: "))
    lotek.append(nrr)
print(lotek)

for index, number in enumerate(lotek):
    if number >= 49 or number < 1:
        print(index, number, "---DUPA!", sep='\t')
