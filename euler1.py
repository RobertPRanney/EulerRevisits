from rr_defs import mults_of_any
factors = [3, 5]
sum_of = 0
for x in mults_of_any(factors, 1000):
    sum_of += x

print "Sum of multiples of", factors, "is", sum_of

# optional one-liner
print "One-liner", sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
