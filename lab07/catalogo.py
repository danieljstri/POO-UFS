from item import Item
from cd import CD
from dvd import DVD

class Catalogo:
    def __init__(self):
        self.__catalogo = list()
    def addItem(self, item):
        self.__catalogo.append(item)
    def removeItem(self, item):
        if item in self.__catalogo:
            self.__catalogo.remove(item)
            return True
        else:
            return False
    def searchItem(self, item):
        if item in self.__catalogo:
            return True
        else:
            return False
    def showAllItems(self):
        for i in self.__catalogo:
            if isinstance(i, CD):
                print(i.getTitle())
        print("\n---------------------------------\n")
        for j in self.__catalogo:
            if isinstance(j, DVD):
                print(j.getTitle())