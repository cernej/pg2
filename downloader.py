import requests


class Downloader:
    def __init__(self):
        self.url = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'
        self.data = {}
    def get(self):
        responce = requests.get(self.url)
        if not responce.ok:
            return None
        for line in responce.text.split('\n')[2:]:
            s = line.split('|')
            if len(s) < 5:
                continue
            # '2,654'.replace(',', '.') -> '2.654'
            # float('2.654') -> 2.654
            self.data[s[3]] = float(s[4].replace(',', '.'))
    def convert_from_czk(self, ammount_czk, code):
        return ammount_czk / self.data[code]


if __name__ == "__main__":
    downloader = Downloader()
    downloader.get()
    print(downloader.convert_from_czk(100, 'USD'))
    