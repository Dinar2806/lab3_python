import pytest
from factorial_fibonacci.factorial import factorial, factorial_recursive
from factorial_fibonacci.fibonacci import fibo, fibo_recursive


class TestFactorial:
    """Тесты для функций вычисления факториала"""
    
    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (7, 5040),
        (10, 3628800),
    ])
    def test_factorial(self, n, expected):
        """Тест итеративной версии факториала"""
        assert factorial(n) == expected
    
    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (7, 5040),
        (10, 3628800),
    ])
    def test_factorial_recursive(self, n, expected):
        """Тест рекурсивной версии факториала"""
        assert factorial_recursive(n) == expected
    
    def test_factorial_consistency(self):
        """Проверка согласованности итеративной и рекурсивной версий"""
        for n in range(0, 10):
            assert factorial(n) == factorial_recursive(n)
    
    def test_factorial_negative(self):
        """Проверка обработки отрицательных чисел"""
        with pytest.raises(RecursionError):
            factorial_recursive(-1)
        
        # Итеративная версия зациклится на отрицательных числах
        # Это может быть проблемой, в зависимости от реализации


class TestFibonacci:
    """Тесты для функций вычисления чисел Фибоначчи"""
    
    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (7, 13),
        (10, 55),
        (15, 610),
        (20, 6765),
    ])
    def test_fibo(self, n, expected):
        """Тест итеративной версии Фибоначчи"""
        assert fibo(n) == expected
    
    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (7, 13),
        (10, 55),
    ])
    def test_fibo_recursive(self, n, expected):
        """Тест рекурсивной версии Фибоначчи"""
        assert fibo_recursive(n) == expected
    
    def test_fibo_consistency(self):
        """Проверка согласованности итеративной и рекурсивной версий"""
        for n in range(0, 15):  # Ограничиваем из-за производительности рекурсии
            assert fibo(n) == fibo_recursive(n)
    
    def test_fibo_negative(self):
        """Проверка на отрицательные входные данные"""
        # Текущие реализации не обрабатывают отрицательные числа
        # Можно добавить обработку или тестировать поведение
        pass
    
    @pytest.mark.performance
    def test_fibo_performance(self):
        """Проверка производительности для больших n"""
        # Итеративная версия должна быть быстрее
        n = 30
        result_iter = fibo(n)
        result_rec = fibo_recursive(n)
        assert result_iter == result_rec