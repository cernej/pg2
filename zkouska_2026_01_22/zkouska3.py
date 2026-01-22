# vytvorte tridni hierarchii Osoba -> Student, Ucitel
# trida Osoba bude mit atributy jmeno a vek, metodu pridej_rok(), ktera vek zvysi o 1
# trida Student bude mit navic atribut rocnik, ktery se bude také zvyšovat metodou pridej_rok(),
# ale pouze pokud rocnik neni vic nez 5 (tzn. pokud je rocnik 5, tak se nezvysi)
# trida Ucitel bude mit navic atributy obor a praxe (pocet let praxe),
# metoda pridej_rok() u Ucitele zvysi pouze praxi o 1 (bez omezení)

class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
    
    def pridej_rok(self):
        self.vek += 1

    def __str__(self):
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"


class Student(Osoba):
    # ZDE DOPLŇTE VÁŠ KÓD
    
    def __str__(self):
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"


class Ucitel(Osoba):
    # ZDE DOPLŇTE VÁŠ KÓD
    
    def __str__(self):
        return f"Ucitel {self.jmeno} uci obor {self.obor} a má {self.praxe} let praxe"


def test_tridy():
    student = Student("Jan", 21, 3)
    assert student.jmeno == "Jan"
    assert student.vek == 21
    assert student.rocnik == 3
    student.pridej_rok()
    assert student.vek == 22
    assert student.rocnik == 4
    student.pridej_rok()
    student.pridej_rok()
    student.pridej_rok()  # rocnik by mel zůstat 5
    assert student.rocnik == 5

    ucitel = Ucitel("Petr", 35, "Matematika", 10)
    assert ucitel.jmeno == "Petr"
    assert ucitel.vek == 35
    assert ucitel.obor == "Matematika"
    assert ucitel.praxe == 10
    ucitel.pridej_rok()
    assert ucitel.vek == 35  # vek by mel zůstat stejný
    assert ucitel.praxe == 11


if __name__ == "__main__":
    student1 = Student("Adam", 23, 5)
    student2 = Student("Eva", 19, 1)
    ucitel = Ucitel("Tomas", 40, "IT", 15)

    osoby = [student1, student2, ucitel]
    for osoba in osoby:
        print(osoba)
        osoba.pridej_rok()
        print("Po přidání roku:")
        print(osoba)