from livro import Livro

class Biblioteca:
    def _init_(self, nome: str):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo} - Autor: {livro.autor.nome}")