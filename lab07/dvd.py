from item import Item

class DVD(Item):
    def __init__(self):
        self.__director = ""
    def getDirector(self):
        return self.__director
    def setDirector(self, newDirector):
        self.__director = newDirector
