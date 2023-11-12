from cd import CD
from dvd import DVD

cd = CD("album 1", 60, "Artista 1", 123456, "Um otimo CD")
dvd = DVD("Filme 1", 120, "Diretor 1", "Um otimo DVD")

cd.inserir_cd(CD('album 3', 30, 'artista 3', 542342, 'pessimo cd'))

if (cd.localizar_por_titulo('album 3')):
  print('existe')
else:
  print('nao existe')

cd.imprimir_todo()

dvd.inserir_dvd(DVD('filme 2', 180, 'diretor 2', 'um bom dvd'))

if dvd.localizar_por_titulo('filme 2'):
  print('existe')
else:
  print('nao existe')

dvd.immprimir_todo()