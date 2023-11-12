from item import Item

class CD(Item):
    def __init__(self):
        self.__artist = ""
        self.__numberTrails = 0
    def getArtist(self):
        return self.__artist
    def getNumberTrails(self):
        return self.__numberTrails
    def setArtist(self, newArtist):
        self.__artist = newArtist
    def setNumberTrails(self, newNumberTrails):
        self.__numberTrails = newNumberTrails