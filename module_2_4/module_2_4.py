numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
NotPrimes = []
for j in numbers:
    if j == 1:
        continue
    drop = False
    for i in range(2, j):
        if j % i == 0:
            drop = True
            break
    if not drop:
        primes.append(j)
    else:
        NotPrimes.append(j)
print(primes)
print(NotPrimes)