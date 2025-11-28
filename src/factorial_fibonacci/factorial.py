

def factorial(n: int) -> int:
    result = 1
    if n == 0 or n == 1: 
        return result
    
    for i in range(1, n+1):
        result *= i

    return result

def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


