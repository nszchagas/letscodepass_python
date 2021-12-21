def isIdade(idadeRecebida, min, max):
  if (idadeRecebida<=min or idadeRecebida>=max):
    print(f'A idadade digitada é invalida. Insira valores entre {min} e {max}.\nTente novamente.\n')
  return idadeRecebida>min and idadeRecebida<max

def isSalario(salarioRecebido, min):
  if (salarioRecebido<=min):
    print(f'O salário digitado é inválido. Insira valores maiores que {min}.\nTente novamente.\n')
  return salarioRecebido>min

def isSexo(sexoRecebido, possibilidades):
  if sexoRecebido.upper() not in possibilidades:
    print(f'O sexo digitado não é válido. Insira uma das opções.')
    print('tente novamente.')
  return sexoRecebido.upper() in possibilidades

while(True):
  idade = int(input('Digite a idade:'))
  IDADEMIN, IDADEMAX = 0, 150
  if (isIdade(idade, IDADEMIN, IDADEMAX)):
    break

while(True):
  salario = float(input('Digite o salario:'))
  SALARIOMIN = 0
  if (isSalario(salario, SALARIOMIN)):
    break

while(True):
  SEXOS_POSSIVEIS = ['M', 'F', 'Outro']
  sexo = input(f'Digite o sexo {SEXOS_POSSIVEIS}:\n')
  if (isSexo(sexo, SEXOS_POSSIVEIS)):
    break




