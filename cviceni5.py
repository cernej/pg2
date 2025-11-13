import sys

def inkrementuj_cisla(data):
    results = []
    for value in data:
        row = []
        for x in value.split(','):
            try:
                x = str(int(x) + 1)
            except ValueError:
                pass
            row.append(x)
        results.append(','.join(row))
    return results

def zapis(file_name, data):
    with open(file_name, "w") as file:
        for line in data:
            file.write(line + '\n')

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f'Pouziti: python {sys.argv[0]} jmeno_souboru')
        sys.exit()

    file_name = sys.argv[1]  # data.csv
    data = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                data.append(line.strip())
    except FileNotFoundError:
        print(f'Soubor {file_name} neexistuje')
        
    data = inkrementuj_cisla(data)

    name = file_name.split('.')  #  name = ['data', 'csv']

    file_name2 = name[0] + '2.' + name[1]  #  'data2.csv'
    zapis(file_name2, data)