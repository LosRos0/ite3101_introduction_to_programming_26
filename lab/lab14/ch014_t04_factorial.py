def factorial(x):
    total = 1

    for n in range(1, x + 1):
        total *= n

    return total