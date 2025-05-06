from Funcionario import Funcionario

novoFuncionario = Funcionario("Luis", "12345678910", 25.50)
print(novoFuncionario.nome, novoFuncionario.cpf, novoFuncionario.valorPorHora)

novoFuncionario.incrementarHoras(8)
print(novoFuncionario.horasTrabalhadas)

novoFuncionario.incrementarHoras(4)
print(novoFuncionario.horasTrabalhadas)

print("Salário:", novoFuncionario.calcularSalario())
