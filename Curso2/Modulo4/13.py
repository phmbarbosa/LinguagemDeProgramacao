try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        print(f"Número de linhas: {len(linhas)}")
        print("\nConteúdo do arquivo:")
        for linha in linhas:
            print(linha.strip())
except FileNotFoundError:
    print("Arquivo 'dados.txt' não encontrado.")
