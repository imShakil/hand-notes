"""
# Prime Generator in Python
# Sieve of Eratosthenes
# David Eppstein
"""

import time


def gen_primes():
    D = {}
    q = 2
    while True and q < 100005:
        if q not in D:
            yield q          # to return primes
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1


t = time.time()
primes = gen_primes()
all_primes = list(primes)
