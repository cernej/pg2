class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
    
    def __str__(self):
        return f'Osoba {self.jmeno} ma {self.vek} let'

    def pridat_rok(self):
        self.vek += 1


class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik=1):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f'Student {self.jmeno} ma {self.vek} let a studuje {self.rocnik} rocnik'
    
    def pridat_rok(self):
        super().pridat_rok()
        if self.rocnik < 5:
            self.rocnik += 1


class Ucitel(Osoba):
    def __init__(self, jmeno, vek, roky_praxe=0):
        super().__init__(jmeno, vek)
        self.roky_praxe = roky_praxe
    
    def __str__(self):
        return f'Ucitel {self.jmeno} ma {self.vek} let a ma {self.roky_praxe} let praxe'

    def pridat_rok(self):
        super().pridat_rok()
        self.roky_praxe += 1


class Udrzbar(Osoba):
    def __str__(self):
        return f'Udrzbar {self.jmeno} ma {self.vek} let'


if __name__ == "__main__":
    student1 = Student("Alice", 19)
    student2 = Student("Bob", 27, 2)
    ucitel1 = Ucitel("Prof", 41)
    udrzbar1 = Udrzbar("Karel", 55)

    osoby = [student1, ucitel1, student2, udrzbar1]
    for osoba in osoby:
        for i in range(10):
            osoba.pridat_rok()
    print(student1)
    print(student2)
    print(ucitel1)
    print(udrzbar1)
    
