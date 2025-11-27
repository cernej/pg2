class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email
    
    def __str__(self):
        return f'Osoba({self.jmeno}, {self.telefon}, {self.email})'

    @property
    def jmeno(self):
        return self.__jmeno

    @jmeno.setter
    def jmeno(self, hodnota: str):
        for c in hodnota:
            if not c.isalpha() and not c.isspace():
                raise InvalidData(f'Chybne zadane jmeno "{hodnota}"')
        self.__jmeno = hodnota

    @property
    def telefon(self):
        return self.__telefon
    
    @telefon.setter
    def telefon(self, hodnota: str):
        if not len(hodnota) == 13:
            raise InvalidData(f'Cislo musi obsahovat 13 znaku')
        if hodnota[0] != '+':
            raise InvalidData(f'Cislo musi zacinat +')
        if not hodnota[1:].isdigit():
            raise InvalidData(f'Neni cislo')
        self.__telefon = hodnota

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, hodnota: str):
        if '@' not in hodnota:
            raise InvalidData(f'Email musi obsahovat @')
        if not hodnota.endswith('.cz'):
            raise InvalidData(f'Email musi koncit .cz')
        if not hodnota.replace('@', '').replace('.', '').isalnum():
            raise InvalidData(f'Email obsahuje nepovolene znaky')
        self.__email = hodnota

if __name__ == "__main__":
    o1 = Osoba("Tomas", "+420777888999", "ahoj1@email.cz")
    print(o1)
    