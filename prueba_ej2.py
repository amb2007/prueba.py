
def filter():
    print('Hola, ¿cómo estás? ¿Podrías ingresar la cantidad de sub listas?')
    tmñ = int(input())
    listagrande = []
    res = []
    for i in range(tmñ):
        print('Ahora dime los números de la lista número', i)
        sublist = list(int( input()))  
        listagrande.append(sublist)
    for j in range(len(listagrande[0])):  
        elementoComun = True
        for i in range(1, tmñ):  
            if listagrande[0][j] != listagrande[i][j]:  
                elementoComun = False
                break
        if elementoComun:
            res.append(listagrande[0][j])
    return res

print(filter())
