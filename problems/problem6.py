def findSum(num):
    return int(num * (num + 1) / 2)

def findSumSquared(num):
    return int((num * (num + 1) * (2 * num + 1)) / 6)

def main():
    num = 100

    sum = findSum(num)
    sumSquared = sum * sum

    squaredSum = findSumSquared(num)

    print(sumSquared - squaredSum)

main()


