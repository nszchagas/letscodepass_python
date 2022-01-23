import csv

def calculaMedia(lista):
  media = 0
  lista = list(map(float, lista))
  if len(lista) > 0:
    for valor in lista:
      media+= valor
    media /= len(lista)
  return media
  
with open('exs_mod3/alunos_media.csv', 'w', encoding='utf-8', newline='\n') as alunosMedia:
  with open('exs_mod3/alunos.csv', 'r', encoding='utf-8') as alunos:
    fr = csv.reader(alunos)
    fw = csv.writer(alunosMedia)
    headers = fr.__next__()
    headers.append('Média')
    fw.writerow(headers)
    for row in csv.reader(alunos):
      matricula, nome, frequencia, *notas = row
      media = calculaMedia(notas)
      row.append(media.__format__('.1f'))
      fw.writerow(row)
