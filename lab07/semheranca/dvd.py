class DVD:

  def __init__(self, titulo, temprep, diretor, comentario):
    self._titulo = titulo
    self._temprep = temprep
    self._diretor = diretor
    self._comentario = comentario
    self.__possuo = True
    self.__lista = []

  def get_titulo(self):
    return self._titulo

  def get_temprep(self):
    return self._temprep

  def get_diretor(self):
    return self._diretor

  def get_comentario(self):
    return self._comentario

  def get_possuo(self):
    return self.__possuo

  def set_titulo(self, titulo):
    self._titulo = titulo

  def set_temprep(self, temprep):
    self._temprep = temprep

  def set_diretor(self, diretor):
    self._diretor = diretor

  def set_comentario(self, comentario):
    self._comentario = comentario

  def set_possuo(self, possuo):
    self.__possuo = possuo

  def inserir_dvd(self, dvd):
    self.__lista.append(dvd)

  def localizar_por_titulo(self, titulo):
    for dvd in self.__lista:
      if dvd.get_titulo() == titulo:
        return dvd
      else:
        print('nao existe')

  def immprimir_todo(self):
    for dvd in self.__lista:
      print('-' * 20)
      print(dvd.get_titulo())
      print(dvd.get_diretor())
      print(dvd.get_temprep())
      print(dvd.get_comentario())