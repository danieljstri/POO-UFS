class CD:
    def __init__(self, titulo, temprep, artista, numtri, comentario):
        self.__titulo = titulo
        self.__temprep = temprep
        self.__artista = artista
        self.__possuo = True
        self.__numtri = numtri
        self.__comentario = comentario
        self.__lista = []

    # Métodos getters e setters

    def get_titulo(self):
        return self.__titulo

    def get_temprep(self):
        return self.__temprep

    def get_artista(self):
        return self.__artista

    def get_numtri(self):
        return self.__numtri

    def get_comentario(self):
        return self.__comentario

    def get_possuo(self):
        return self.__possuo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_temprep(self, temprep):
        self.__temprep = temprep

    def set_artista(self, artista):
        self.__artista = artista

    def set_numtri(self, numtri):
        self.__numtri = numtri

    def set_comentario(self, comentario):
        self.__comentario = comentario

    def set_possuo(self, possuo):
        self.__possuo = possuo

    def inserir_cd(self, cd):
        self.__lista.append(cd)

    def localizar_por_titulo(self, titulo):
        for cd in self.__lista:
            if cd.get_titulo() == titulo:
                return cd
        print('Não existe')

    def imprimir_todo(self):
        for cd in self.__lista:
            print('-' * 20)
            print(cd.get_titulo())
            print(cd.get_temprep())
            print(cd.get_artista())
            print(cd.get_numtri())
            print(cd.get_comentario())