import pickle

numeros = [10, 20, 30, 40, 50]

with open("dados.bin", "wb") as arquivo:
    pickle.dump(numeros, arquivo)

with open("dados.bin", "rb") as arquivo:
    numeros_lidos = pickle.load(arquivo)

print("Números lidos do arquivo binário:")
print(numeros_lidos)
