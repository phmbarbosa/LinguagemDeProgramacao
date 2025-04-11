class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}, {self.paginas} páginas"

    def __len__(self):
        return self.paginas

livro = Livro("1984", "George Orwell", 328)

print(str(livro))
print(f"Número de páginas: {len(livro)}")
