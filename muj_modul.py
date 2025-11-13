def fibonacci(maximum):
    result = [1, 1]
    value = 2
    while value <= maximum:
        result.append(value)
        value = result[-2] + result[-1]
    return result


if __name__ == "__main__":
    import sys
    maximum = int(sys.argv[1])
    print(fibonacci(maximum))