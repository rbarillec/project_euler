def Euler0002():
    max = 4e6
    i = 0
    sum = 0
    
    fib1 = 0
    fib2 = 1
    
    while fib2 < max:
        print(fib2)
        if (fib2 %2 == 0):
            sum += fib2
        fib1, fib2 = fib2, fib2 + fib1
    print("The sum is", sum)

Euler0002()
