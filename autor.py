from pessoa import Pessoa

class Autor(Pessoa):
    def _init_(self, nome: str, cpf: str):
        super()._init_(nome, cpf)