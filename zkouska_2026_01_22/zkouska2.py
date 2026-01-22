# vas program nacte ze souboru, ktery dostane jako argument z prikazove radky, text a vypise ho pozpatku
# vytvorte funkci pozpatku(), ktera jako parametr bere text a vraci ho pozpatku tzn "ahoj" -> "joha"
# osetrete chybove stavy pomoci try - except
import sys


def pozpatku(text):
    text_pozpatku = ""

    # ZDE DOPLŇTE VÁŠ KÓD

    return text_pozpatku


def test_pozpatku():
    assert pozpatku("ahoj") == "joha"
    assert pozpatku("Python") == "nohtyP"
    assert pozpatku("") == ""
    assert pozpatku("A") == "A"
    assert pozpatku("12345") == "54321"


if __name__ == "__main__":
    try:
        soubor = sys.argv[1]
        with open(soubor, "r") as fp:
            obsah = fp.read()
            obracene = pozpatku(obsah)
            print(obracene)
    except IndexError:
        print("Zadej nazev souboru")
    except FileNotFoundError:
        print("Soubor neexistuje")