class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Vektor({self.x}, {self.y})'
    
    def secti(self, jiny_vektor):
        x = self.x + jiny_vektor.x
        y = self.y + jiny_vektor.y
        return Vektor(x, y)

    def vynasob(self, skalar):
        x = self.x * skalar
        y = self.y * skalar
        return Vektor(x, y)


if __name__ == "__main__":

    v1 = Vektor(10, 5)
    v2 = Vektor(10, 10)

    v3 = v1.secti(v2)
    print(v3)

    v4 = v3.vynasob(3)
    print(v4)