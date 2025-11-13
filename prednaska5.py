import csv



if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru k nacteni: ")
        output_data = []
        
        with open(name, "r") as file:
            reader = csv.reader(file)
            for i, data in enumerate(reader, 1):
                data.append(i)
                print(data)
                #output_data.append(data)
        
        # name = input("Zadej jmeno souboru k zapisu: ")
        # with open(name, "w") as file:
        #     writer = csv.writer(file)
        #     writer.writerows(output_data)

    except FileNotFoundError as e:
        print(f'Soubor {name} neexistuje')