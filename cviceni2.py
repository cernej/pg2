def prace_se_seznamem():
    # vytvorime seznam (list) o 4 prvcich
    seznam = [100, 5, 3, 21]
    print(seznam)
    # vezmeme 3. prvek a vynasobime ho 2
    seznam[2] *= 2
    print(seznam)
    # na konec seznamu pridame novy prvek
    seznam.append(55)
    print(seznam)
    # seznam setridime vzestupne
    seznam.sort()
    print(seznam)
    # otocime poradi prvku v seznamu
    seznam.reverse()
    print(seznam)


def vrat_treti_prvek(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None

def prumer(cisla):
    return sum(cisla) / len(cisla)

def naformatuj_text(student):
    vek = student["vek"]
    obor = student["obor"]
    znamky = student["znamky"]
    prumer_znamek = prumer(znamky)
    zaokrouhleno = round(prumer_znamek, 2)
    text = f"Student: {student["jmeno"]} {student["prijmeni"]}, Vek: {vek}, Obor: {obor}, Prumer: {zaokrouhleno}"
    return text

if __name__ == "__main__":
    #prace_se_seznamem()
    #vrat_treti_prvek([1,2,3,4])
    #prumer(cisla)

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,3,1,2,1]
    }
    student["vek"] += 1
    student["obor"] = "AEFP"
    print(naformatuj_text(student))
    student["prumer"] = "abc"