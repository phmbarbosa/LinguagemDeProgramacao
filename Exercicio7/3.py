dicionario = {
    "cachorro": "dog",
    "gato": "cat",
    "pássaro": "bird",
    "amor": "love",
    "feliz": "happy"
}

palavra_pt = input("Digite uma palavra em português: ")
if palavra_pt in dicionario:
    print(f"A tradução de {palavra_pt} é {dicionario[palavra_pt]}.")
else:
    print("Tradução não encontrada.")
