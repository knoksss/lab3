class Queue:
    # реализация структуры данных очередь (FIFO) 
    def __init__(self):
        self.items = []
    

    def enqueue(self, x: int) -> None:
        # добавляет элемент в конец очереди
        self.items.append(x)  # добавляем в конец
    

    def dequeue(self) -> int:
        # удаляет и возвращает первый элемент очереди
        if self.is_empty():
            raise IndexError('ERROR: Удаление из пустой очереди')
        return self.items.pop(0)  # удаляем из начала
    

    def front(self) -> int:
        # возвращает первый элемент без удаления
        if self.is_empty():
            raise IndexError('ERROR: Берётся значение из пустой очереди')
        return self.items[0]
    

    def is_empty(self) -> bool:
        # проверяет, пуста ли очередь
        return len(self.items) == 0
    
    
    def size(self) -> int:
        # возвращает размер очередиSS
        return len(self.items)   