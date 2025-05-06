from pessoa import Pessoa

class Funcionario(Pessoa):
    def _init_(self, nome: str, cpf: str):
        super()._init_(nome, cpf)