import math
from typing import Set

number = 600851475143
seen = set()

def findFactors(num):
    factors = []
    maxNumber = int(math.sqrt(num))

    if num in seen:
        return [-1]

    for i in range(2, maxNumber):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))

    result = []

    for fact in factors:
        result.extend(findFactors(fact))

    if len(result) == 0:
        result.append(num)

    seen.add(num)

    return result

def main():
    factors_list = findFactors(number)

    factors_list.sort()
    # print("factors: {}".format(factors_list))
    print("max prime factor: {}".format(max(factors_list)))

main()

