from funcionario import Funcionario
from autor import Autor

f = Funcionario("Carlos", "123.456.789-00")
a = Autor("Fernanda", "987.654.321-00")

print(f"Funcionário: {f.nome}, CPF: {f.cpf}")
print(f"Autor: {a.nome}, CPF: {a.cpf}")