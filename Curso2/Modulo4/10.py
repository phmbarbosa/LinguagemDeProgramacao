def contar_pares(n):
    for i in range(0, n+1, 2):
        yield i

limite = int(input("Gerar números pares até: "))
for numero in contar_pares(limite):
    print(numero)
