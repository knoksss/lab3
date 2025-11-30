class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []  # вспомогательный стек для хранения минимумов
    

    def push(self, x: int) -> None:
        # добавляет элемент на вершину стека
        self.items.append(x)
        
        # обновляем min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    
    def pop(self) -> int:
        # удаляет и возвращает элемент с вершины стека
        if self.is_empty():
            raise IndexError('ERROR: Удаление из пустого стека')
        value = self.items.pop()
        
        # обновляем min_stack
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    
    def peek(self) -> int:
        # возвращает элемент с вершины без удаления
        if self.is_empty():
            raise IndexError('ERROR: Берётся значение из пустого стека')
        return self.items[-1]
    
    
    def is_empty(self) -> bool:
        # проверяет, пуст ли стек
        return len(self.items) == 0
    
    
    def size(self) -> int:
        # возвращает размер стека
        return len(self.items)
    
    
    def min(self) -> int:
        # возвращает минимальный элемент в стеке за O(1)
        if self.is_empty():
            raise IndexError('ERROR: Берётся минимум из пустого стека')
        return self.min_stack[-1]