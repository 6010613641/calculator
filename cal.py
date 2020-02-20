def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


if __name__ == '__main__':
    #a, b = input("Enter number a, b: ").split()
    #a = int(a)
    #b = int(b)

    print(add(5, 10) == 15)
    print(sub(5, 10) == -5)
    print(mul(5, 10) == 50)
    print(div(5, 10) == 0.5)
