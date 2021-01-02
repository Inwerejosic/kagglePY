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


# from the assignments

def sign(x):
    if x < 0:
        return(-1)  # it's negative
    elif x == 0:
        return(0)  # it's zero
    elif x > 0:
        return(1)  # it's positive

sign(-1)


def to_smash(total_candies):
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")

to_smash(91)
to_smash(1)

# or 

def to_smash(total_candies):
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

to_smash(91)
to_smash(1)
