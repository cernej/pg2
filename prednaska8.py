import sys
import json

class InvalidData(Exception):
    pass

class Car:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva
    
    def __str__(self):
        return f'Auto: {self.znacka} / {self.model} / {self.barva}'

    @classmethod
    def parse(cls, jdata):
        data = json.loads(jdata)
        for value in ('znacka', 'model', 'barva'):
            if value not in data:
                raise InvalidData(f'Missing {value} in data')
        return cls(data['znacka'], data['model'], data['barva'])


if __name__ == "__main__":

    data = [
        '{"znacka": "bmw", "barva": "modra"}',
        '{"znacka": "toyota", "model": "corrola", "barva": "cervena"}',
        '{"znacka": "mercedes", "model": "slk", "barva": "cerna"}',
        '{"znacka": "trabant", "model": "600"}'
    ]

    for item in data:
        try:
            auto = Car.parse(item)
            print(auto)
        except InvalidData as e:
            print(e)