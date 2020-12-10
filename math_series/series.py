# lab

# Fibonacci
def fibonacci(n):
    x = 0
    y = 1
    i = 0
    while i <= n - 3:
        test = x
        x = y
        y = x + test
        if (i == n - 3):
            return y
        i += 1

# Lucas
def lucas(n):
    x = 2
    y = 1
    i = 0
    while i <= n - 3:
        test = x
        x = y
        y = x + test
        if (i == n - 3):
            return y
        i += 1

# Sum Series
def sum_series(n, x=0, y=1):
    i = 0
    while i <= n - 3:
        test = x
        x = y
        y = x + test
        if (i == n - 3):
            return y
        i += 1