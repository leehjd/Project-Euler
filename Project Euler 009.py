# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

def pythagorean(n):
    for a in range(1,n):
        for b in range(a,n):
            c = sqrt(a**2 + b**2)
            if c % 1 == 0:
                if a + b + int(c) == 1000:
                    print(a*b*int(c))

pythagorean(1000)