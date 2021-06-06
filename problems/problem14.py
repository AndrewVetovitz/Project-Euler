def findLongestSequence(total):
    previous = {}
    longest = 0
    largestNumber = -1

    for i in range(1, total - 1):
        currLen = 1
        temp = i

        while i != 1:
            if i in previous:
                currLen += previous[i]
                break

            if i % 2 == 0:
                i /= 2
            else:
                i = i * 3 + 1

            currLen += 1

        previous[temp] = currLen


        if currLen > longest:
            longest = currLen
            largestNumber = temp

        longest = max(longest, currLen)

    return largestNumber

def main():

    length = 1_000_000

    longest = findLongestSequence(length)

    print("longest sequence: {}".format(longest))

main()
