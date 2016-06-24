def IsDivisibleBy(value, factors):
    for factor in factors:
        if value % factor == 0:
            return True
    return False

def Euler0003(value):
    factors = []
    factorProduct = 1
    candidate = 1
    
    while (factorProduct < value) and (candidate / value < value):
        candidate += 1
        if (value % candidate == 0) and (not IsDivisibleBy(candidate, factors)):
            factors.append(candidate)
            factorProduct *= candidate
            print(candidate)

    print("The largest prime factor of ", value, " is ", factors[-1]) 

Euler0003(600851475143)
