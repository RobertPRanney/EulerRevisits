from rr_defs import fib_nums_value

sum_of = 0
for x in fib_nums_value(1, 2, 4000000):
    if x % 2 == 0:
        sum_of += x

print "Sum of fib sequence 1,2... under 4mil is", sum_of

# optional one-liners
print "One-liner", sum([x for x in fib_nums_value(1, 2, 4000000) if x % 2 == 0])
