import math
from typing import Set
largest = 21

def findMaxFactors(num, factorsCount, primes):
    i = 1
    curr = {}

    for i in primes:
        while num != 0 and num % i == 0:
            num = num / i

            if not i in curr:
                curr[i] = 0

            curr[i] = curr[i] + 1

    for key in curr.keys():
        if not key in factorsCount:
            factorsCount[key] = 0
        
        factorsCount[key] = max(factorsCount[key], curr[key])

def main():
    primes = [2]
    nums = []

    for i in range(largest):
        nums.append(True)

    for i in range(3, len(nums)):
        if nums[i]:
            primes.append(i)

            if i > 0:
                for j in range(i, len(nums), i):
                    nums[j] = False

    factorCounts = {}

    for i in range(largest):
        findMaxFactors(i, factorCounts, primes)

    mult = 1

    for key in factorCounts.keys():
        count = factorCounts[key]

        while count > 0:
            count -= 1
            mult *= key

    print(mult)

main()


