from rr_defs import is_prime

nums = [2, 3, 2, 5, 7, 2, 3, 11, 13, 2, 17, 19]

print reduce(lambda x, y: x * y, nums)