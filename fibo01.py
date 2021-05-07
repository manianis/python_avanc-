def fibo(n):
    a = b = 1
    print(a)
    print(b)
    while a <= n:
        a, b = a + b, a
        print(a)


fibo(100)
