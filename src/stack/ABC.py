from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def pop(self) -> int:
        """Удаляет и возвращает верхний элемент"""
        # Должно бросать исключение при пустом стеке
    
    @abstractmethod
    def push(self, x: int) -> None:
        """Добавляет элемент на вершину стека"""
    
    @abstractmethod
    def peek(self) -> int:
        """Возвращает верхний элемент без удаления"""
        # Должно бросать исключение при пустом стеке
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек"""
    
    @abstractmethod
    def __len__(self) -> int:
        """Возвращает количество элементов"""
    
    @abstractmethod
    def min(self) -> int:
        """Возвращает минимальный элемент за O(1)"""
        # Должно бросать исключение при пустом стеке



    @abstractmethod
    def print_elements(self) -> None:
        """Вывод всех элементов стека"""
        
