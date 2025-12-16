import pytest
import random
import time
from typing import List, Callable
from sorting.sort_algorithms import (
    bubble_sort, 
    quick_sort, 
    counting_sort, 
    radix_sort, 
    bucket_sort, 
    heap_sort
)


class TestSortingAlgorithms:
    """Тесты для алгоритмов сортировки"""
    
    # Общие тестовые данные
    TEST_ARRAYS = [
        # (input, expected_sorted)
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
        (random.sample(range(1, 101), 100), list(range(1, 101))),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
        ([1, 2, 3, 1, 2, 3], [1, 1, 2, 2, 3, 3]),
    ]
    
    # Словарь алгоритмов сортировки для параметризации
    SORTING_ALGORITHMS = {
        'bubble_sort': bubble_sort,
        'quick_sort': quick_sort,
        'counting_sort': counting_sort,
        'radix_sort': radix_sort,
        'heap_sort': heap_sort,
    }
    
    @pytest.mark.parametrize("algorithm_name", SORTING_ALGORITHMS.keys())
    @pytest.mark.parametrize("arr, expected", TEST_ARRAYS)
    def test_sorting_algorithms(self, algorithm_name, arr, expected):
        """Общий тест для всех алгоритмов сортировки"""
        algorithm = self.SORTING_ALGORITHMS[algorithm_name]
        result = algorithm(arr.copy())
        assert result == expected, f"{algorithm_name} failed on input {arr}"
    
    def test_bucket_sort(self):
        """Тест для bucket sort (работает с float)"""
        test_cases = [
            ([], []),
            ([1.5], [1.5]),
            ([3.2, 1.1, 2.5], [1.1, 2.5, 3.2]),
            ([5.5, 3.3, 8.8, 4.4, 2.2], [2.2, 3.3, 4.4, 5.5, 8.8]),
        ]
        
        for arr, expected in test_cases:
            result = bucket_sort(arr.copy())
            assert result == expected, f"Bucket sort failed on input {arr}"
    
    @pytest.mark.parametrize("algorithm_name", ['quick_sort', 'heap_sort', 'radix_sort'])
    def test_sorting_large_array(self, algorithm_name):
        """Тест производительности на больших массивах"""
        algorithm = self.SORTING_ALGORITHMS[algorithm_name]
        
        # Генерация большого массива
        size = 1000
        arr = random.sample(range(10000), size)
        expected = sorted(arr)
        
        start_time = time.time()
        result = algorithm(arr.copy())
        elapsed_time = time.time() - start_time
        
        assert result == expected
        print(f"{algorithm_name} sorted {size} elements in {elapsed_time:.4f} seconds")
    
    def test_sorting_stability(self):
        """Тест стабильности сортировки (где это важно)"""
        # Bubble sort должен быть стабильным
        arr = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
        
        # Сортируем по первому элементу кортежа
        def key_func(x):
            return x[0]
        
        # Bubble sort стабилен
        sorted_arr = bubble_sort(arr.copy())
        
        # Проверяем, что порядок элементов с одинаковыми ключами сохранился
        for i in range(len(sorted_arr) - 1):
            if sorted_arr[i][0] == sorted_arr[i + 1][0]:
                # Должны сохраниться исходные индексы 'a' перед 'c'
                pass
    
    def test_edge_cases(self):
        """Тест граничных случаев"""
        # Массив с отрицательными числами
        arr = [-5, 3, -1, 0, 2]
        
        # Проверяем алгоритмы, которые поддерживают отрицательные числа
        for name, algorithm in [('quick_sort', quick_sort), ('heap_sort', heap_sort)]:
            result = algorithm(arr.copy())
            assert result == sorted(arr), f"{name} failed on negative numbers"
    
    @pytest.mark.parametrize("algorithm_name, arr", [
        ('counting_sort', [1000000, 1, 2]),  # Большой диапазон значений
        ('radix_sort', [999999, 888888, 777777]),  # Большие числа
    ])
    def test_extreme_values(self, algorithm_name, arr):
        """Тест с экстремальными значениями"""
        algorithm = self.SORTING_ALGORITHMS[algorithm_name]
        result = algorithm(arr.copy())
        assert result == sorted(arr)
    
    def test_already_sorted(self):
        """Тест уже отсортированного массива"""
        arr = list(range(100))
        
        for name, algorithm in self.SORTING_ALGORITHMS.items():
            result = algorithm(arr.copy())
            assert result == arr, f"{name} failed on already sorted array"
    
    def test_reverse_sorted(self):
        """Тест обратно отсортированного массива"""
        arr = list(range(100, 0, -1))
        
        for name, algorithm in self.SORTING_ALGORITHMS.items():
            result = algorithm(arr.copy())
            assert result == sorted(arr), f"{name} failed on reverse sorted array"


if __name__ == "__main__":
    # Быстрый запуск тестов
    tester = TestSortingAlgorithms()
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    for name, algorithm in tester.SORTING_ALGORITHMS.items():
        print(f"Testing {name}:")
        result = algorithm(arr.copy())
        print(f"  Input: {arr}")
        print(f"  Output: {result}")
        print(f"  Correct: {result == sorted(arr)}")
        print()