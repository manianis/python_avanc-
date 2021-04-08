def fibo(n):
    a = b = 1
    yield a
    yield b
    while a <= n:
        a, b = a + b, a
        yield a


for v in fibo(100):
    print(v)
