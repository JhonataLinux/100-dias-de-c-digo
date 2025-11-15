empresa = {
    101: {'nome': 'Ana Silva', 'cargo': 'Analista', 'salario': 5500},
    102: {'nome': 'Isabela bandira', 'cargo': 'Gerente', 'salario': 6000},
    103: {'nome': 'Moise fernado', 'cargo': 'vendedor', 'salario': 1800  },
    104: {'nome': 'victor', 'cargo': 'aprendiz', 'salario': 800},
}

def processar_cadastro(empresa, id_funcionario, percentual_aumento):
     percentual_aumento = 1 + (percentual_aumento/100)
     if id_funcionario in empresa:
         print(f" ID do funcionario existe: {id_funcionario}")
         salario_atual = empresa[id_funcionario]['salario']
         novo_salario = salario_atual * percentual_aumento
         empresa[id_funcionario]['salario'] = novo_salario
     else:
         print(f"ERRO ID {id_funcionario}: não encontrado")

processar_cadastro(empresa, 101,10)
processar_cadastro(empresa, 102,50)
processar_cadastro(empresa, 103,15)
processar_cadastro(empresa, 104,25)
print(empresa)