def vrat_treti(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None


def prumer(cisla):
    # vrati soucet hodnot v promenne cisla vydeleny jejich poctem
    return sum(cisla) / len(cisla)


def naformatuj_text(zak):
    jmeno = zak["jmeno"]
    prijmeni = zak["prijmeni"]
    vek = zak["vek"]
    prumer_znamek = round(prumer(zak["znamky"]), 2)
    return f"Student: {jmeno} {prijmeni}, Vek: {vek}, Prumer znamek: {prumer_znamek}"

if __name__ == "__main__":
    # vytvorime novy seznam (list)
    seznam = [12, 50, 1, 3, 5]
    # vezmeme 3. prvek a vynasobime tremi
    seznam[3] *= 3
    # na konec seznamu pripojime hodnotu 100
    seznam.append(100)
    # seznam setridime a otocime poradi prvku
    seznam.sort()
    seznam.reverse()

    student = {
        "jmeno": "Tomas",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,1,3,1,2,1]
    }
    student["vek"] += 1
    vysledek = naformatuj_text(student)
    print(vysledek)

