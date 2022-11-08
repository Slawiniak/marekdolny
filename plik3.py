def max(lista):
    rezultat = lista[0]
    for element in lista:
        if element > rezultat:
            rezultat = element
    return rezultat
moja_lista = [4, 2, 5, 8, 23, 90, -3, 0, 72]
