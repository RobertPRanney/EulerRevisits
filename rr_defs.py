from math import floor, sqrt, ceil


def mults_of_all(factors, end):
    """
    yield all integers that have all nums in factors as a factor
    :param factors: list of factors
    :param end: generator stops here
    """
    num = 1
    while num < end:
        if [num % factor == 0 for factor in factors].count(True) == len(factors):
            yield num
        num += 1


def mults_of_any(factors, end):
    """
    yield numbers under end with any number in factor list as a factor
    :param factors:
    :param end:
    """
    num = 1
    while num < end:
        if [num % factor == 0 for factor in factors].count(True) >= 1:
            yield num
        num += 1


def fib_nums_terms(first, second, terms):
    """
    yield fib sequence one by one for a given start
    num(term) = num(term-1) + num(term-2)
    :param first: 1st number of fib sequence
    :param second: 2nd number of fib sequence
    :param terms: number of terms to generate
    """
    current = first
    next_num = second
    num = 1

    while num <= terms:
        yield current
        holder = current
        current = next_num
        next_num += holder
        num += 1


def fib_nums_value(first, second, value):
    """
    yield fib terms til a certain value
    fib(term) = fib(term-1) + fib(term-2)
    :param first: 1st term of fib sequence
    :param second: 2nd term of fib sequence
    :param value: max value to go till
    """
    current = first
    next_num = second

    while current <= value:
        yield current
        holder = current
        current = next_num
        next_num += holder


def is_prime(n):
    """
    Checks if a certain number is in fact prime
    :param n: number to check
    :return: True if prime, else False
    """
    if n <= 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        roof = floor(sqrt(n))
        check = 5
        while check <= roof:
            if n % check == 0:
                return False
            if n % (check + 2) == 0:
                return False
            check += 6

    return True


def prime_gen(stop):
    """
    yield a sequence of primes until stop point
    uses is prime to check every number til stop point
    :param stop: last prime to check
    """
    for num in xrange(stop):
        if is_prime(num):
            yield num


def factor_gen(num):
    """
    yield all factors of given number
    :param num:
    :return:
    """
    for check in xrange(1, num+1):
        if num % check == 0:
            yield check


def is_palindrome(num):
    """
    returns True if reverse of number is forward of number
    :param num:
    :return:
    """
    check = str(num)
    for x in range(len(check)):
        if check[x] != check[-(x+1)]:
            return False
    return True


def prime_factorization(num):
    factors = []
    rem = num
    while not is_prime(rem):
        test = 2
        while rem % test != 0:
            test += 1
        factors.append(test)
        rem = rem / test
    factors.append(rem)
    return factors