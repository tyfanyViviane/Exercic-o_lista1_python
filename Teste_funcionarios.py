from funcionario_clt import FuncionarioCLT
from funcionario_horista import FuncionarioHorista

clt = FuncionarioCLT("Maria", 3000.0)
horista = FuncionarioHorista(25.0, 160)

print(f"{clt.nome} (CLT) - Salário: R${clt.calcularSalario()}")
print(f"Funcionário Horista - Salário: R${horista.calcularSalario()}")