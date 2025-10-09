
if __name__ == "__main__":
    # konverze ze str na int
    hodnota1 = input("Zadej cislo: ")
    hodnota1 = int(hodnota1)

    operator = input("Zadej operator (+, -, *, /): ")
    # konverze ze str na int
    hodnota2 = input("Zadej cislo: ")
    hodnota2 = int(hodnota2)

    # formatovany string (text)
    print(f"Operace: {hodnota1} {operator} {hodnota2} =")

    # nastav "nic" dokud v promenne neni vysledek operace
    vysledek = None
    # podminka slozena z vice vetvi if-elif-...-else
    if operator == "+":
        vysledek = hodnota1 + hodnota2
    elif operator == "-":
        vysledek = hodnota1 - hodnota2
    elif operator == "*":
        vysledek = hodnota1 * hodnota2
    elif operator == "/":
        if hodnota2 == 0:
            print("Nelze delit nulou")
        else:
            vysledek = hodnota1 / hodnota2
    # do teto vetve se dostaneme, pokud zadna nadrazena nebyla provedena
    else:
        print(f"Neznamy operator '{operator}'")

    # porovnani promenne a None pro vyhodnoceni uspesnosti operace
    if vysledek == None:
        print("Operace se nezdarila")
    else:
        print(f"Vysledek operace: {vysledek}")