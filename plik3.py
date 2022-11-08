def max(lista):
    rezultat = lista[0]
    for element in lista:
        if element > rezultat:
            rezultat = element
    return rezultat
