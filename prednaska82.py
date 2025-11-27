from abc import ABC, abstractmethod
import math

class Tvar(ABC):
    @abstractmethod
    def spocitej_obsah(self):
        return None

    def __str__(self):
        return f'Tento geometricky tvar ma obsah: {self.spocitej_obsah()}'

class Obdelnik(Tvar):
    def __init__(self, sirka, delka):
        self.sirka = sirka
        self.delka = delka
    
    def spocitej_obsah(self):
        return self.sirka * self.delka


class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer

    def spocitej_obsah(self):
        return math.pi * self.polomer * self.polomer


if __name__ == "__main__":

    obj = Obdelnik(2,3)
    print(obj)