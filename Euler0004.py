# Project Euler - Problem 4
# -----------------------------
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalyndrom(intValue):
    value = str(intValue)
    return value == value[::-1]

def Palyndrome(numberOfDigits):
    min = 10 ** (numberOfDigits-1)
    max = (10 ** (numberOfDigits)) - 1
    
    values = range(max, min-1, -1)
    largestPalyndrome = 0

    for i in values:
        for j in range(i, min-1, -1):
            product = i*j
            if IsPalyndrom(product) and (product > largestPalyndrome):
                largestPalyndrome = product

    if largestPalyndrome > 0:
        print ("Largest palyndrom of 2 ", numberOfDigits, "digit numbers is ", largestPalyndrome)
    else:
        print ("No palyndrom of 2 ", numberOfDigits, "digit numbers could be found")

Palyndrome(3)