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