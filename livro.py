from autor import Autor

class Livro:
    def _init_(self, titulo: str, autor: Autor):
        self.titulo = titulo
        self.autor = autor