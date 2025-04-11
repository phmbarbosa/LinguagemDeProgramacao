def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(10))
print(triplo(5))
