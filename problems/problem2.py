def main():
    sum = 0
    one = 0
    two = 1

    while True:
        temp = one + two
        one = two
        two = temp

        if two > 4_000_000:
            break

        if temp % 2 == 0:
            sum += temp

    print("sum: {}".format(sum))

main()
