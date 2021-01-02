def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)


# More on conditional functions

def g(x):
    if x > 0:
        print("Only printed when x is positve; x =", x)
        print("Also only printed when x is positive; x =", x)
        print("Always printed, regardless of x's value; x =", x)

g(1)
#g(0)
#g(-1)

