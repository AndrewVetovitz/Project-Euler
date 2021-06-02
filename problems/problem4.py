import math
from typing import Set

def main():
    maxPal = -1

    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            mult = i * j

            if isPalindrome(mult):
                maxPal = max(maxPal, mult)

    print(maxPal)

def isPalindrome(num):
    strNum = str(num)
    left = 0
    right = len(strNum) - 1

    while left < right:
        if strNum[left] != strNum[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

main()
