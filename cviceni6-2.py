import requests
import sqlite3

db = sqlite3.connect('sqlite.db')

def download_rates(url):
    response = requests.get(url, timeout=2)
    if not response.ok:
        return None
    
    rates = {}

    data = response.text
    data = data.split('\n')
    date = data[0].split('#')[0].strip()
    
    for line in data[2:]:
        fields = line.split('|')
        if len(fields) < 5:
            continue
        rates[fields[3]] = float(fields[4].replace(',', '.'))

    return date, rates


if __name__ == "__main__":

    db.execute('CREATE TABLE IF NOT EXISTS rates (date TEXT, currency TEXT, rate REAL)')

    datum, listek = download_rates('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt')
    
    for currency, rate in listek.items():
        db.execute('INSERT INTO rates VALUES (?, ?, ?)', (datum, currency, rate))
    
    db.commit()
    