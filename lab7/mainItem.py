from catalogo import Catalogo
from cd import CD
from dvd import DVD
from item import Item

def main():
    cd1 = CD()
    cd1.setTitle("Escandalo Intimo")
    cd2 = CD()
    cd2.setTitle("Montero")
    dvd1 = DVD()
    dvd1.setTitle("Onde esta Terca-Feira?")
    dvd2 = DVD()
    dvd2.setTitle("O Protetor")
    cataloguinho = Catalogo()
    cataloguinho.addItem(cd1)
    cataloguinho.addItem(cd2)
    cataloguinho.addItem(dvd1)
    cataloguinho.addItem(dvd2)
    #cataloguinho.removeItem(cd1)
    #cataloguinho.removeItem(dvd2)
    cataloguinho.showAllItems()

if __name__=="__main__":
    main()
