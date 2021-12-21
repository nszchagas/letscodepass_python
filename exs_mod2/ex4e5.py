
meses = {
  'Janeiro': 31, 
  'Fevereiro': 28,
  'Marco':31, 
  'Abril':30, 
  'Maio':31, 
  'Junho':30, 
  'Julho':31, 
  'Agosto':31,
  'Setembro':30, 
  'Outubro':31, 
  'Novembro':30,
  'Dezembro':31
}

for mes in meses.keys():
  print(f'{mes}: {meses[mes]} dias')
