from abc import ABC, abstractmethod
from collections import deque
from stack.ABC import Stack



class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

class LinkedList(Stack):
    def __init__(self):
        self.top = None
        self._size = 0
        self.min_node = None  # для отслеживания минимума
    
    def push(self, x: int) -> None:
        new_node = Node(x, self.top)
        self.top = new_node
        self._size += 1
        
        # Обновление минимума
        if self.min_node is None or x < self.min_node.value:
            self.min_node = Node(x, self.min_node)
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        
        # Обновляем минимум если нужно
        if value == self.min_node.value:
            self.min_node = self.min_node.next
            
        return value
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value
    
    def is_empty(self) -> bool:
        return self.top is None
    
    def __len__(self) -> int:
        return self._size
    
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Min from empty stack")
        return self.min_node.value
    


    def print_elements(self):
        if self.is_empty():
            raise IndexError("Попытка вывести элементы из пустого стека")
        
        current_element = self.top
        output = []

        while current_element is not None:
            output.append(current_element)
            current_element = current_element.next

        return output





class ListStack:
    def __init__(self):
        self._items = []
        self._min_stack = []  # Дополнительный стек для минимумов
    
    def push(self, x: int) -> None:
        self._items.append(x)
        
        # Обновляем стек минимумов
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        
        value = self._items.pop()
        
        # Обновляем стек минимумов
        if value == self._min_stack[-1]:
            self._min_stack.pop()
            
        return value
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def __len__(self) -> int:
        return len(self._items)
    
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Min from empty stack")
        return self._min_stack[-1]
    

    def print_elements(self):
        return self._items
    




class QueueStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self._min = None
    
    def push(self, x: int) -> None:
        self.queue1.append(x)
        
        # Обновляем минимум
        if self._min is None or x < self._min:
            self._min = x
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Удаление из пустого стека")
        
        # Перекладываем все элементы кроме последнего в queue2
        while len(self.queue1) > 1:
            item = self.queue1.popleft()
            self.queue2.append(item)
        
        value = self.queue1.popleft()
        
        # Меняем очереди местами
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        # Нужно пересчитать минимум после pop
        if value == self._min:
            self._recalculate_min()
            
        return value
    
    def _recalculate_min(self):
        """Пересчитывает минимум после удаления элемента"""
        if self.is_empty():
            self._min = None
            return
        
        self._min = min(self.queue1)
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        
        # Аналогично pop, но сохраняем последний элемент
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        value = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return value
    
    def is_empty(self) -> bool:
        return len(self.queue1) == 0
    
    def __len__(self) -> int:
        return len(self.queue1)
    
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Min from empty stack")
        return self._min
    


    def print_elements(self):
        if self.is_empty():
            raise IndexError("Попытка вывести элементы из пустого стека")
        
        q1 = self.queue1
        q2 = self.queue2
        
        


if __name__ == "__main__":
    stack = QueueStack()
    stack.push(11)
    stack.push(22)
    stack.push(45)
    stack.push(52)
    stack.push(5252)
    print(stack.print_elements())



