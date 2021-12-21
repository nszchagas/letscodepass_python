perguntas = ['Mora perto da vítima?', 
'Já trabalhou com a vítima?', 
'Telefonou para a vítima?', 
'Esteve no local do crime?', 
'Devia para a vítima?']

pontuacao = 0 #quantidade de sim's


def getSituacao(pontuacao):
  if pontuacao <= 1:
    return 'Liberado.'
  elif pontuacao == 2:
    return 'Suspeito.'
  elif pontuacao <= 4:
    return 'Cúmplice.'
  elif pontuacao == 5:
    return 'Assassinos.'

print("Responda as perguntas a seguir com sim ou não.\n")
for pergunta in perguntas: 
  if input(pergunta+'\n').lower() == 'sim':
    pontuacao+=1

print(getSituacao(pontuacao))


