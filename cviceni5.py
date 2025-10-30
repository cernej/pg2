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


def zapis_data_do_csv(file_name, data):
    with open(file_name, "w") as file:
        for row in data:
            # row2 = [str(value) for value in row]
            # for value in row:
            #     row2.append(str(value))
            line = ','.join([str(value) for value in row])
            file.write(line + '\n')


if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru: ")  # data.txt -> data + txt
        file = open(name, "r")
        results = precti_hodnoty_a_incrementuj(file)
        file.close()
        name, ext = name.split('.')
        file_name = name + '2.' + ext # zapis hodnot z result do data2.txt
        zapis_data_do_csv(file_name, results)
    except FileNotFoundError:
        print(f'Soubor {name} neexistuje')