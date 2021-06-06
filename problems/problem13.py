def findSum(file):
    lines = open(file)
    finalSum = 0

    for line in lines:
        finalSum += int(line)

    return finalSum


def main():
    sum = findSum('../files/13.txt')

    print("sum: {}".format(sum))

main()
