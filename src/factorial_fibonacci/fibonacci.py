def fibo(n: int) -> int:
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(n-1):
        a = b
        b = a + b
    return b

def fibo_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

