def findLargestProduct(content, width):
    maxProduct = 0
    currProduct = 1
    left = 0

    for right in range(len(content)):
        if right - left + 1 > width:
            currProduct /= int(content[left])
            left += 1

        if content[right] == '0':
            left = right + 1
            currProduct = 1
            continue

        currProduct *= int(content[right])
        maxProduct = max(maxProduct, currProduct)

    return int(maxProduct)

def main():
    file = open('../files/8.txt', 'r')
    content = file.read()

    joinedContent = content.replace("\n", "")
    
    maxWidth = 13
    largestProduct = findLargestProduct(joinedContent, maxWidth)

    print(largestProduct)

    file.close()

main()
