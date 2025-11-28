def fibo(n):
    """Итеративное вычисление n-го числа Фибоначчи"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibo_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo_recursive(n - 2) + fibo_recursive(n - 1)

