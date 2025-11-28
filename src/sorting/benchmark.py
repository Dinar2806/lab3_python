import time
from src.sorting.sort_algorithms import *
from tests.tests_generate import *

algos = {
    "bubble sort": bubble_sort,
    "heap sort": heap_sort,
    "quick sort": quick_sort,
    "radix sort": radix_sort,
    "counting sort": counting_sort,
    
}
float_algos = {
    "bucket sort": bucket_sort
}

arrays = {
    # Случайные массивы разных размеров
    "random_10": rand_int_array(10, 1, 100, seed=42),
    "random_50": rand_int_array(50, 1, 500, seed=42),
    "random_100": rand_int_array(100, 1, 1000, seed=42),
    "random_500": rand_int_array(500, 1, 5000, seed=42),
    "random_1000": rand_int_array(1000, 1, 10000, seed=42),
    "random_5000": rand_int_array(5000, 1, 50000, seed=42),
    
    # Случайные массивы с уникальными значениями
    "random_unique_100": rand_int_array(100, 1, 1000, distinct=True, seed=42),
    "random_unique_500": rand_int_array(500, 1, 5000, distinct=True, seed=42),
    
    # Почти отсортированные массивы
    "nearly_sorted_100_5": nearly_sorted(100, 5, seed=42),
    "nearly_sorted_1000_10": nearly_sorted(1000, 10, seed=42),
    "nearly_sorted_1000_50": nearly_sorted(1000, 50, seed=42),
    
    # Массивы с дубликатами
    "many_duplicates_100_3": many_duplicates(100, 3, seed=42),
    "many_duplicates_500_5": many_duplicates(500, 5, seed=42),
    "many_duplicates_1000_10": many_duplicates(1000, 10, seed=42),
    
    # Обратно отсортированные массивы
    "reverse_sorted_100": reverse_sorted(100),
    "reverse_sorted_1000": reverse_sorted(1000),
    "reverse_sorted_range_100": reverse_sorted_with_range(100, 1, 1000),
    "reverse_sorted_range_500": reverse_sorted_with_range(500, 1, 5000),
    
}
float_arrays = {
    "float_random_10": rand_float_array(10, seed=42),
    "float_random_50": rand_float_array(50, seed=42),
    "float_random_100": rand_float_array(100, seed=42),
    "float_random_500": rand_float_array(500, seed=42),
    "float_random_1000": rand_float_array(1000, seed=42),
}


def timeit_once(func, *args, **kwargs) -> float:
    start_time = time.perf_counter()
    func(*args, **kwargs)  # Выполняем функцию
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    results = {}

    for algos_name, algos_func in algos.items():
        results[algos_name] = {}

        for array_name, array in arrays.items():
            time_taken = timeit_once(algos_func, array.copy())
            results[algos_name][array_name] = time_taken

    return results

benchmark = benchmark_sorts(arrays, algos)



        
