lista = list(map(int, input("Digite os itens da lista separados por vírgula:").split(',')))

qtdPares = 0

for item in lista:
  if item % 2 == 0:
    qtdPares += 1

print(f'Há {qtdPares} número(s) par(es) na lista: {lista}.')
