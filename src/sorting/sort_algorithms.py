from typing import *
from src.utils import *
from tests.tests_generate import *


float_arr = [float(x) for x in [1,2,3,23,23,24,5,4,7,56,3,42,3,13,24,35,67,45,3,2,4,5464,5,45,34,23,34,5,23,235,34,5,24,45,2,34,36,63,67,2,34]]
arr = [1,2,3,23,23,24,5,4,7,56,3,42,3,13,24,35,67,45,3,2,4,5464,5,45,34,23,34,5,23,235,34,5,24,45,2,34,36,63,67,2,34]



def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return sorted_arr


def quick_sort(arr: List[int]) -> List[int]:
    length = len(arr)
    if length <= 1:
        return arr
    
    pivot = arr[length // 2]
    left_part = [x for x in arr if x < pivot]
    middle_part = [x for x in arr if x == pivot]
    right_part = [x for x in arr if x > pivot]

    return quick_sort(left_part) + middle_part + quick_sort(right_part)


def counting_sort(arr: List[int]) -> List[int]:
    lengh = len(arr)
    if lengh <= 1:
        return arr
    
    # Находим максимальный элемент
    max_val = max(arr)
    
    # Создаем массив для подсчета
    count = [0] * (max_val + 1)
    
    # Подсчитываем количество каждого элемента
    for num in arr:
        count[num] += 1
    
    # Восстанавливаем отсортированный массив
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr


def radix_sort(arr: List[int]) -> List[int]:
    length = len(arr)
    if length <= 1:
        return arr
    
    max_radix = len(str(max(arr)))
    exp = 0

    while exp < max_radix:
        arr = counting_sort_for_radix(arr, exp)
        exp += 1

    return arr

        

    
def bucket_sort(arr: List[float], bucket_size: int = 5) -> List[float]:
    if len(arr) <= 1:
        return arr
    
    min_value= min(arr)
    max_value = max(arr)

    bucket_count = int((max_value - min_value) // bucket_size) + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        bucket_index = int((num - min_value) // bucket_size)
        buckets[bucket_index].append(num)

    sorted_arr = []
    for bucket in buckets:
        if bucket_size > 20:
            sorted_arr.extend(sorted(bucket)) 
        else:
            sorted_arr.extend(insertion_sort(bucket))

    return sorted_arr


def heap_sort(arr: List[int]) -> List[int]:
    
    n = len(arr)
    
    # 1. Построение max-кучи из массива
    # Начинаем с последнего родителя (n//2 - 1)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 2. Извлечение элементов из кучи по одному
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень (максимум) в конец
        arr[i], arr[0] = arr[0], arr[i]
        # Вызываем heapify на уменьшенной куче
        heapify(arr, i, 0)
    
    return arr
    

    






