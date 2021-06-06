def findTriplet(sum):
    for a in range(sum):
        for b in range(a + 1, sum): 
            c = sum - a - b

            if c > b and a * a + b * b == c * c:
                print("a: {} b: {} c: {}".format(a, b, c))
                return a * b * c

    return -1

def main():
    product = findTriplet(1000)

    print(product)

main()
