qtdExercicios = int(input("Digite a quantidade de exercicios:"))
destino = input("Digite o caminho para os arquivos:")

for num in range(1, qtdExercicios+1):
  with open(f'{destino}\ex{num}.py', 'w') as file:
    file.write('')