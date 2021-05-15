def lpf(n):
    pf = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            pf = i
            n /= i
        else:
            i += 1

    if pf < n:
        pf = n

    return pf


print(lpf(600851475143))
