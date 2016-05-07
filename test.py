from sympy import isprime as mod_prime_test
from rr_defs import is_prime as my_prime_test
from time import time
mod_found = 0
my_found = 0
ceiling = 1000000

print "Module Testing....."
symstart = time()
for x in xrange(ceiling):
    if mod_prime_test(x):
        mod_found += 1
symend = time()
print "Module Answer", mod_found

print "My Testing........"
mystart = time()
for x in xrange(ceiling):
    if my_prime_test(x):
        my_found += 1
myend = time()
print "My Answer: ", my_found

print "Built in: ", symend - symstart
print "Mine: ", myend - mystart