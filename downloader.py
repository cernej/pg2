import requests
from unittest.mock import MagicMock


class Downloader:
    def __init__(self):
        self.url = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'
        self.data = {}
        self.get()

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


def test_downloader_nok():
    requests.get = MagicMock(
        # jakoby nam requests.get vratil responce, kde je responce.ok == False
        return_value=MagicMock(
            ok=False
        )
    )
    downloader = Downloader()
    assert downloader.get() == None
    assert len(downloader.data) == 0

def test_dowloader():
    requests.get = MagicMock(
        return_value=MagicMock(
            ok=True,
            text="""03.12.2025 #234
země|měna|množství|kód|kurz
USA|dolar|1|USD|20,000"""
    ))
    downloader = Downloader()
    assert round(downloader.convert_from_czk(100, 'USD'), 2) == 5.0


if __name__ == "__main__":
    downloader = Downloader()
    print(downloader.convert_from_czk(100, 'USD'))
    