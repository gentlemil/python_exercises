liczby = [5,66,13,7,9,3,11,15,6,18,10,24,32]
sorted_ = False
while not sorted_:
    sorted_ = True
    for i in range (1, len(liczby)):     #liczymy od drugiego elem. listy
        if liczby[i-1] > liczby[i]:
            liczby[i-1], liczby[i] = liczby[i], liczby[i-1]     #TO SA DWIE TUPLE, HUEHUE
            sorted_ = False
print(liczby)

# sprytne