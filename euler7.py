primes = [2]
test = 3

while len(primes) < 10001:
    is_prime = True
    for num in primes:
        if test % num == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(test)
    test += 1

print primes[-1]