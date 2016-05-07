from rr_defs import factor_gen, is_prime
test_num = 600851475143
ceiling = 10000

print max([x for x in xrange(ceiling) if is_prime(x) and test_num % x == 0])