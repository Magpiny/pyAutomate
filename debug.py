# print some patterns

def shape(symbol, width, height):

    if (width < 4) or (height < 4):
        raise Exception("Width and Height must be greater or equal to 2")

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    print(symbol * width)


shape("f", 3, 4)
