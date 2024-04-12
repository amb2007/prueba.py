def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sumValues(mtr):
    res = 0
    for i in range(len(mtr)):
        for j in range(len(mtr[0])):
            if (i + j) % 2 != 0 and isPrime(mtr[i][j]):
                res += mtr[i][j]
    return res

# Ejemplo de uso
mtr = [
    [13, 7, 5],
    [11, 7, 3],
    [19, 17, 31]
]

resultado = sumValues(mtr)
print(resultado)
