import pytest
from stack.stack import LinkedList, ListStack, QueueStack


class TestStackInterface:
    """Базовые тесты для интерфейса стека"""
    
    @pytest.fixture(params=[LinkedList, ListStack, QueueStack])
    def stack(self, request):
        """Фикстура для создания всех типов стеков"""
        return request.param()
    
    def test_push_pop(self, stack):
        """Тест базовых операций push/pop"""
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        assert stack.pop() == 30
        assert stack.pop() == 20
        assert stack.pop() == 10
    
    def test_peek(self, stack):
        """Тест операции peek (просмотр верхнего элемента)"""
        stack.push(10)
        assert stack.peek() == 10
        
        stack.push(20)
        assert stack.peek() == 20
        
        stack.pop()
        assert stack.peek() == 10
    
    def test_is_empty(self, stack):
        """Тест проверки пустоты стека"""
        assert stack.is_empty() == True
        
        stack.push(10)
        assert stack.is_empty() == False
        
        stack.pop()
        assert stack.is_empty() == True
    
    def test_len(self, stack):
        """Тест получения размера стека"""
        assert len(stack) == 0
        
        stack.push(10)
        assert len(stack) == 1
        
        stack.push(20)
        stack.push(30)
        assert len(stack) == 3
        
        stack.pop()
        assert len(stack) == 2
    
    def test_min_operation(self, stack):
        """Тест операции получения минимума"""
        stack.push(5)
        assert stack.min() == 5
        
        stack.push(3)
        assert stack.min() == 3
        
        stack.push(7)
        assert stack.min() == 3
        
        stack.push(2)
        assert stack.min() == 2
        
        stack.pop()  # Удаляем 2
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 7
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 3
        assert stack.min() == 5
    
    def test_empty_stack_errors(self, stack):
        """Тест ошибок при работе с пустым стеком"""
        with pytest.raises(IndexError):
            stack.pop()
        
        with pytest.raises(IndexError):
            stack.peek()
        
        with pytest.raises(IndexError):
            stack.min()
    
    def test_duplicate_values(self, stack):
        """Тест с дублирующимися значениями"""
        stack.push(5)
        stack.push(3)
        stack.push(3)  # Дубликат минимума
        stack.push(7)
        
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 7
        assert stack.min() == 3
        
        stack.pop()  # Удаляем первый 3

        
        stack.pop()  # Удаляем второй 3
        assert stack.min() == 5


class TestLinkedListStack:
    """Специфичные тесты для LinkedList реализации стека"""
    
    @pytest.fixture
    def stack(self):
        return LinkedList()
    
    def test_linked_list_internal_structure(self, stack):
        """Тест внутренней структуры связного списка"""
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        # Проверяем через print_elements
        elements = stack.print_elements()
        assert elements == [30, 20, 10]
    
    def test_min_after_pop(self, stack):
        """Тест обновления минимума после pop"""
        stack.push(5)
        stack.push(3)
        stack.push(7)
        stack.push(2)
        stack.push(8)
        
        assert stack.min() == 2
        
        stack.pop()  # Удаляем 8
        assert stack.min() == 2
        
        stack.pop()  # Удаляем 2
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 7
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 3
        assert stack.min() == 5


class TestListStack:
    """Специфичные тесты для List реализации стека"""
    
    @pytest.fixture
    def stack(self):
        return ListStack()
    
    def test_list_stack_internal_structure(self, stack):
        """Тест внутренней структуры списка"""
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        elements = stack.print_elements()
        assert elements == [10, 20, 30]
    
    def test_min_stack_consistency(self, stack):
        """Тест согласованности основного стека и стека минимумов"""
        stack.push(5)
        assert len(stack._items) == 1
        assert len(stack._min_stack) == 1
        
        stack.push(3)
        assert len(stack._min_stack) == 2
        
        stack.push(7)  # Не минимум
        assert len(stack._min_stack) == 2  # Не добавляется в min_stack
        
        stack.push(2)
        assert len(stack._min_stack) == 3


class TestQueueStack:
    """Специфичные тесты для Queue реализации стека"""
    
    @pytest.fixture
    def stack(self):
        return QueueStack()
    
    def test_queue_stack_operations(self, stack):
        """Тест операций стека на основе очередей"""
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        assert stack.pop() == 30
        assert stack.peek() == 20
        assert stack.pop() == 20
        assert stack.pop() == 10
    
    def test_min_recalculation(self, stack):
        """Тест пересчета минимума"""
        stack.push(5)
        stack.push(3)
        stack.push(7)
        
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 7
        assert stack.min() == 3
        
        stack.pop()  # Удаляем 3 (минимум)
        # Здесь должен произойти пересчет
        assert stack.min() == 5
    
    def test_multiple_operations(self, stack):
        """Тест множественных операций"""
        operations = [
            ('push', 10),
            ('push', 5),
            ('push', 15),
            ('pop', 15),
            ('min', 5),
            ('push', 3),
            ('min', 3),
            ('pop', 3),
            ('min', 5),
            ('pop', 5),
            ('min', 10),
            ('pop', 10),
        ]
        
        for op, value in operations:
            if op == 'push':
                stack.push(value)
            elif op == 'pop':
                assert stack.pop() == value
            elif op == 'min':
                assert stack.min() == value
    
    def test_queue_consistency(self, stack):
        """Тест согласованности внутренних очередей"""
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        # После каждой операции должны быть правильные состояния
        assert len(stack.queue1) == 3
        
        stack.pop()
        assert len(stack.queue1) == 2
        
        stack.pop()
        assert len(stack.queue1) == 1
        
        stack.pop()
        assert len(stack.queue1) == 0
        assert len(stack.queue2) == 0


class TestPerformance:
    """Тесты производительности"""
    
    @pytest.mark.performance
    def test_push_pop_performance(self):
        """Тест производительности операций push/pop"""
        import time
        
        implementations = [LinkedList, ListStack, QueueStack]
        num_operations = 1000
        
        for impl in implementations:
            stack = impl()
            
            start_time = time.time()
            
            # Множественные push операции
            for i in range(num_operations):
                stack.push(i)
            
            # Множественные pop операции
            for i in range(num_operations):
                stack.pop()
            
            elapsed_time = time.time() - start_time
            print(f"{impl.__name__}: {num_operations} push/pop operations took {elapsed_time:.4f} seconds")
            
            # Проверяем, что стек пуст
            assert stack.is_empty()


if __name__ == "__main__":
    # Быстрый запуск тестов
    print("Testing LinkedList:")
    stack = LinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Elements: {stack.print_elements()}")
    print(f"Min: {stack.min()}")
    
    print("\nTesting ListStack:")
    stack = ListStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Elements: {stack.print_elements()}")
    print(f"Min: {stack.min()}")
    
    print("\nTesting QueueStack:")
    stack = QueueStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Elements in queue1: {list(stack.queue1)}")
    print(f"Min: {stack.min()}")