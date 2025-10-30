
def precti_hodnoty_a_incrementuj(file):

    all_results = []
    for line in file:
        data = line.split(',')
        result = []
        for value in data:
            value = value.strip().strip('"')
            try:
                value = int(value) + 1
            except ValueError:
                pass
            result.append(value)
        all_results.append(result)
    return all_results



if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru: ")
        file = open(name, "r")
        results = precti_hodnoty_a_incrementuj(file)
        print(results)
    except FileNotFoundError:
        print(f'Soubor {name} neexistuje')