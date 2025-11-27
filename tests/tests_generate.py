from typing import *


import random



def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> List[int]:
    if seed is not None:
        random.seed(seed)  # Фиксируем последовательность
    
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Недостаточно уникальных значений в диапазоне")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]
    

def nearly_sorted(n: int, swaps: int, *, seed=None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    
    arr = list(range(1, n + 1))

    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]

    return arr

def many_duplicates(n: int, k_unique=5, *, seed=None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    
    # Создаем k_unique уникальных чисел
    unique_numbers = random.sample(range(1, 100), k_unique)

    output_arr = [random.choice(unique_numbers) for _ in range(n)]
    return output_arr



def reverse_sorted_with_range(n: int, lo: int, hi: int) -> List[int]:
    arr = sorted([random.randint(lo, hi) for _ in range(n)])
    return [arr[len(arr) - i] for i in range(1, n + 1)]


def reverse_sorted(n: int) -> List[int]:
    return list(range(n, 0, -1))



def rand_float_array(n: int, lo=0.0, hi=1.0, *, distinct=False, seed=None) -> List[float]:
    if seed is not None:
        random.seed(seed)
    
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Недостаточно уникальных значений в диапазоне")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.uniform(lo, hi) for _ in range(n)]

