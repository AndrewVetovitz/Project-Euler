import math

def findPrimes(n):
    primes = [2]

    for i in range(3, n, 2):
        sqrt = math.sqrt(i)

        for j in range(len(primes)):
            prime = primes[j]

            if i % prime == 0:
                break

            if prime > sqrt or j == len(primes) - 1:
                primes.append(i)
                break

    return primes

def main():
    primes = findPrimes(2_000_000)

    primeSum = sum(primes)

    print("sum: {}".format(primeSum))

main()
