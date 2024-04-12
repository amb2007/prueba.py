def intersect():
    lista1 = [1,2,3,4,5]
    lista2 = [3,4,5,6,7]
    largo1 = len(lista1)
    largo2 = len(lista2)
    res = []
    i = 0
    j = 0
    for i in range(largo1):
        for j in range(largo2):
            if lista1[i] == lista2[j] and lista1[i] not in res:
                res.append(lista1[i])
    return res
print(intersect())