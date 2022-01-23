import csv

with open('exs_mod3/alunos_copia.csv', 'w', encoding='utf-8', newline='\n') as alunosCopia:
  with open('exs_mod3/alunos.csv', 'r', encoding='utf-8') as alunos:
    for row in csv.reader(alunos):
      csv.writer(alunosCopia, ).writerow(row)
