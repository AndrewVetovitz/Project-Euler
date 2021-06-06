
import math

def findPrimes(totalPrimes):
    primes = [2, 3]
    curr = 4

    while len(primes) < totalPrimes:
        bound = math.sqrt(curr)

        for prime in primes:
            if prime > bound:
                primes.append(curr)
                break

            if curr % prime == 0:
                break

        curr += 1
    
    return primes

def main():
    primes = findPrimes(10001)

    # print(primes)
    print("len of list: {}".format(len(primes)))
    print(primes[-1])

main()
