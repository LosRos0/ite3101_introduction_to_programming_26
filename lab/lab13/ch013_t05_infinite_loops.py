count = 0
def is_prime(x):
    if x <= 1:
        return False

    for n in range(2, x):
        if x % n == 0:
            return False

    return True

while count < 10:  # Add a colon
    print(count)
    # Increment count
