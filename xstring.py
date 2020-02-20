def add(x, y):
    return x + y


def length(x):
    return len(x)


def substr(x, i):  # slicing
    return x[i+1:]


if __name__ == '__main__':
    print(substr("Hello", 2) == "llo")
    print(substr("Hello", 2) != "lo")
