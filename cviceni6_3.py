from cviceni6_2 import download_rates
import sys


def currencies_ammount(amount_czk, rates):
    result = {}
    for currency, rate in rates.items():
        result[currency] = amount_czk / rate
    return result


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit()
    amount = int(sys.argv[1])

    date, rates = download_rates('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt')

    conversions = currencies_ammount(amount, rates)

    for currency, conversion in conversions.items():
        print(currency, conversion)
