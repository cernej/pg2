def my_range(start, stop, step=1):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    result = []
    hodnota = start
    while hodnota < stop:
        result.append(hodnota)
        hodnota += step
    return result

def for_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    result = []

    for prvek in iterable:
        result.append( (start, prvek) )
        start += 1

    return result

def while_enumerate(iterable, start=0):
    result = []
    index = 0
    while index < len(iterable):
        result.append( (index + start, iterable[index]) )
        index += 1
    return result

# def my_zip(*iterables):
#     pass


if __name__ == "__main__":

    print(list(enumerate(['Alice', 'Bob', 'Eva'], 100)))
    print(for_enumerate(['Alice', 'Bob', 'Eva'], 100))
    print(while_enumerate(['Alice', 'Bob', 'Eva'], 100))

    # my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])

    # print(list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])))
    # print(my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"]))