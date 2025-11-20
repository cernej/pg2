class ChybnaCastka(Exception):
    pass


class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0
    
    def vloz(self, suma):
        if suma <= 0:
            raise ChybnaCastka("Nelze pridat nulovou nebo zapornou castku")
        self.__zustatek += suma

    def vyber(self, suma):
        if suma <= 0:
            raise ChybnaCastka("Nelze pridat nulovou nebo zapornou castku")
        if suma > self.__zustatek:
            raise ChybnaCastka("Nemuzeme vybrat vic, nez mame na uctu")
        self.__zustatek -= suma

    def __str__(self):
        return f'Ucet vlastni {self.jmeno} a je na nem {self.__zustatek} kc'


if __name__ == "__main__":
    try:
        ucet = BankovniUcet("Alice")
        print(ucet)

        ucet.__zustatek = -1000

        ucet.vloz(100)
        print(ucet)

        ucet.vyber(50)
        print(ucet)

        ucet.vloz(10)
        print(ucet)

        ucet.vyber(60)
        print(ucet)
    except ChybnaCastka as e:
        print(e)