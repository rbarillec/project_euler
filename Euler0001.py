def Euler0001():
    max = 1000
    sum = 0
    for i in range(1, max):
        if i%3 == 0 or i%5 == 0:
            sum += i

    print(sum)

Euler0001()