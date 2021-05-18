from math import log, ceil


def prime_number(limit):
    n = [True] * (limit + 1)
    n[0] = n[1] = False

    for (i, is_prime) in enumerate(n):
        if is_prime:
            yield i
            for j in range(i * i, limit + 1, i):
                n[j] = False


def upper_limit(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def number_of_primes(n):
    primes = list(prime_number(upper_limit(n)))
    return primes[n - 1]

print(number_of_primes(10001))
