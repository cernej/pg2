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


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f'Pouziti: python {sys.argv[0]} jmeno_souboru')
        sys.exit()

    file_name = sys.argv[1]
    data = []

    with open(file_name, "r") as file:
        for line in file:
            data.append(line.strip())

    print(data)  # ['Alice,25,student', 'Bob,22,pracujici']

    data = inkrementuj_cisla(data)

    print(data)  # ['Alice,26,student', 'Bob,23,pracujici']
