x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
abs1 = abs(x)
abs2 = abs(y)
smallest_abs = min(abs1, abs2)
print(smallest_abs)


# using it in a function

def f(x):
    y = abs(x)
    return y

print(f(5))