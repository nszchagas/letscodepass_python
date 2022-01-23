import csv

with open('exs_mod3/alunos.csv', 'r', encoding='utf-8') as alunos:
  fr = csv.reader(alunos)
  fr.__next__()
  for row in fr:
    matricula, nome, frequencia, *notas = row
    notas = ', '.join(notas)
    print(f'{matricula} - {nome} - Frequência: {frequencia} - Notas: {notas}.')
  
  