def faktorial(n):
    # funkce vypocita faktorial:
    # 0! -> 1
    # 1! -> 2
    # 5! -> 120
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)


def faktorial2(n):
    # spocita faktorial pomoci cyklu
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":

    print(f"Rekurzivni faktorial: 0! = {faktorial(0)}")
    print(f"Faktorial pomoci cyklu: 0! = {faktorial2(0)}")
    print(f"Rekurzivni faktorial: 1! = {faktorial(1)}")
    print(f"Faktorial pomoci cyklu: 1! = {faktorial2(1)}")
    print(f"Rekurzivni faktorial: 5! = {faktorial(5)}")
    print(f"Faktorial pomoci cyklu: 5! = {faktorial2(5)}")
    print(f"Rekurzivni faktorial: 100! = {faktorial(100)}")
    print(f"Faktorial pomoci cyklu: 100! = {faktorial2(100)}")