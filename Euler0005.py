# Project Euler - Problem 4
# -----------------------------
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def IsDivisibleByAll(value, factors):
    for factor in factors[::-1]:
        if value % factor != 0:
            return False
    return True

def IsDivisibleByAny(value, factors):
    for factor in factors:
        if value % factor == 0:
            return True
    return False

def GetPrimeFactors(number):
    primeFactors = [2]
    for i in range(3, number+1):
        if not IsDivisibleByAny(i, primeFactors):
            primeFactors.append(i)
    return primeFactors
    
def Euler(number):
    factors = range(2, number+1)
    candidate = number

    print("Smallest number evenly divisible by all numbers up to ", number, "is", candidate)

Euler(20)
