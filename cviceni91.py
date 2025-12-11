# napište funkci filtruj_cisla(typ, cisla), která přijme dva parametry:
# typ – řetězec, který může nabývat hodnot "kladna", "zaporna", "suda", "licha"
# cisla – seznam čísel
# Funkce vrátí nový seznam obsahující pouze ta čísla z parametru cisla, která odpovídají zadanému typu.

def filtruj_cisla(typ, cisla):
    vysledek = []

    for c in cisla:
        if typ == "kladna" and c > 0:
            vysledek.append(c)
        elif typ == "zaporna" and c < 0:
            vysledek.append(c)
        elif typ == "suda" and c % 2 == 0:
            vysledek.append(c)
        elif typ == "licha" and c % 2 != 0:
            vysledek.append(c)

    # if typ == "kladna":
    #     for c in cisla:
    #         if c > 0:
    #             vysledek.append(c)
    # elif typ == "zaporna":
    #     for c in cisla:
    #         if c < 0:
    #             vysledek.append(c)
    # elif typ == "suda":
    #     for c in cisla:
    #         if c % 2 == 0:
    #             vysledek.append(c)
    # elif typ == "licha":
    #     for c in cisla:
    #         if c % 2 != 0:
    #             vysledek.append(c)
 
    return vysledek


if __name__ == "__main__":
    print(filtruj_cisla("kladna", [1, -2, 0, 5, -3]))   # [1, 5]
    print(filtruj_cisla("suda", [1, 2, 3, 4, 5]))       # [2, 4]
    print(filtruj_cisla("zaporna", [1, -2, 0, 5, -3]))   # [-2, -3]
    print(filtruj_cisla("licha", [1, 2, 3, 4, 5]))       # [1, 3, 5]
    # neexistující typ
    print(filtruj_cisla("xxx", [1, 2, 3]))              # []