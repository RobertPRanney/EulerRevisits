from rr_defs import is_palindrome as pal

print max([x*y for x in range(100, 1000) for y in range(100, 1000) if pal(x*y)])
