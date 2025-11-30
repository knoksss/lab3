from src.stc.stack_func import Stack
from src.que.queue_func import Queue
import pytest


def test_stack():
        stack = Stack()
        
        # добавляем элементы
        for i in [5, 3, 7, 2, 8, 1]:
            stack.push(i)
        
        assert stack.size() == 6
        assert stack.peek() == 1
        assert stack.min() == 1
        
        # удаляем несколько элементов
        assert stack.pop() == 1
        assert stack.min() == 2
        assert stack.pop() == 8
        assert stack.min() == 2
        assert stack.pop() == 2
        assert stack.min() == 3
        
        # добавляем новые элементы
        stack.push(0)
        assert stack.min() == 0
        stack.push(4)
        assert stack.min() == 0
        
        assert stack.size() == 5
        assert stack.items == [5, 3, 7, 0, 4]


def test_peek_empty_stack():
        stack = Stack()
        with pytest.raises(IndexError, match="ERROR: Берётся значение из пустого стека"):
            stack.peek()

    
def test_queue():
        queue = Queue()
        
        # добавляем элементы
        for i in range(1, 6):
            queue.enqueue(i)
        
        assert queue.size() == 5
        assert queue.front() == 1
        
        # удаляем несколько элементов
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.front() == 3
        assert queue.size() == 3
        
        # добавляем новые элементы
        queue.enqueue(6)
        queue.enqueue(7)
        
        assert queue.size() == 5
        assert queue.items == [3, 4, 5, 6, 7]
        
        # удаляем оставшиеся
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.dequeue() == 6
        assert queue.dequeue() == 7
        assert queue.is_empty() == True


def test_dequeue_empty_queue():
        queue = Queue()
        with pytest.raises(IndexError, match="ERROR: Удаление из пустой очереди"):
            queue.dequeue()