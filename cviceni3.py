def my_range(start, stop, step=1):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    result = []
    actual = start
    while actual < stop:
        result.append(actual)
        actual += step
    return result

def for_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    result = []
    index = start
    for el in iterable:
        result.append( (index, el) )
        index += 1
    return result

def while_enumerate(iterable, start=0):
    result = []
    index = 0
    while index < len(iterable):
        result.append( (start + index, iterable[index]) )
        index += 1
    return result

# def my_zip(*iterables):
#     pass


if __name__ == "__main__":

    # text = "abcdef"
    # print(list(enumerate(text)))
    # print(while_enumerate(text))
    # print(for_enumerate(text))

    # print(list(enumerate(['Alice', 'Bob', 'Eva'])))
    # print(for_enumerate(['Alice', 'Bob', 'Eva']))

    # my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])

    print(list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])))
    # print(my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"]))