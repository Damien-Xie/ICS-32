
#global
x = 50
y = 100


def fun(x, y):
    x += 1
    y += 1
    # Point 2
    return bar(x, y)


def bar(a, b):
    # Point 3
    # print (a, b, c, x, y)
    return a + b


def main():
    #locals
    a = 10
    b = 20

    # Point 1
    # print(a, b, c, x, y)
    c = fun(a, b)
    # Point 4
    print(a, b, c, x, y)

# prints 10, 20, 32, 50, 100

main()
