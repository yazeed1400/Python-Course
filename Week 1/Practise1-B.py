x = float(input("x: "))

if (x < -100):
    print(-x)
elif (x >= -100 and x <= -25):
    print(x ** 4)
elif (x > -25 and x <= 0):
    print(3 * (x ** 2) - 1)
elif (0 < x and x <= 100):
    print((3.14 / 2) * x + 3 ** x)
elif (x > 100):
    print(x)
