user = int(raw_input("High End?"))
lop = []

for check in xrange(2, user):
    is_prime = True
    test = 2
    while test < check and is_prime:
        if check % test == 0:
            is_prime = False
        test += 1

    if is_prime:
        lop.append(check)


print lop