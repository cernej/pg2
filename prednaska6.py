from muj_modul import fibonacci
import random
import time
import requests


def hraci_automat():
    symboly = ['🍒', '🍋', '🍊', '🍇', '🔔', '💎', '7️⃣']

    #random.seed(10)
    steps = 0
    while True:
        steps += 1
        vysledek = []
        for i in range(3):
            vysledek.append(random.choice(symboly))
        print(vysledek)
        if len(set(vysledek)) == 1:
            print(f"VYHRAL JSI na {steps} pokus!!!")
            break


if __name__ == "__main__":
    # fib = fibonacci(10)
    # print(list(reversed(fib)))
    
    ts = time.time()
    
    #hraci_automat()

    print('Jdu spat...')
    time.sleep(5)
    print('... pokracuju')

    print(f'Program bezel: {(time.time() - ts)} s')


