from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

autor1 = Autor("Machado de Assis", "123.456.789-10")
livro1 = Livro("Dom Casmurro", autor1)
livro2 = Livro("Memórias Póstumas de Brás Cubas", autor1)

bib = Biblioteca("Biblioteca Central")
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

print(f"Livros da {bib.nome}:")
bib.listar_livros()       