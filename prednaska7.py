import math
from abc import ABC, abstractmethod

class Tvar(ABC):
    @abstractmethod
    def obsah(self):
        pass


class Ctverec(Tvar):
    def __init__(self, hrana):
        self.hrana = hrana

    def obsah(self):
        return self.hrana * self.hrana


class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer
    
    def obsah(self):
        return math.pi * self.polomer * self.polomer


if __name__ == "__main__":

    obj = Tvar()

    tvary = [Ctverec(2), Ctverec(3), Kruh(2), Ctverec(1), Kruh(3), Ctverec(2.5)]

    suma = 0
    for tvar in tvary:
        suma += tvar.obsah()
    print(f'Suma vsech tvaru je: {suma}')


    # obj1 = Ctverec(6)
    # print(obj1.obsah())
    # obj2 = Kruh(3)
    # print(obj2.obsah())