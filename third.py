import time

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """
    return False

def je_prvocislo2(cislo):
    if cislo <= 1:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True


if __name__ == "__main__":
    cislo = int(input("Zadej cislo: "))

    je_neni = None
    if je_prvocislo2(cislo):
        je_neni = 'je'
    else:
        je_neni = 'neni'

    print(f'Cislo {cislo} {je_neni} prvocislo')

    
    print(1000000000/3600/24/365)
