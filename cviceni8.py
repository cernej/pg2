class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email
    
    def __str__(self):
        return f'Osoba({self.jmeno}, {self.telefon}, {self.email})'


if __name__ == "__main__":

    o1 = Osoba("12345", "+420777888999", "ahoj@email.cz")
    print(o1)
