from sys import stdin
from src.que.queue_func import Queue
from src.errors import InvalidInputError, QueueEmptyError


def queue_interactive(queue: Queue):
    print("Доступные команды:")
    print("enqueue <число> - добавить элемент")
    print("dequeue - удалить первый элемент")
    print("front - посмотреть первый элемент")
    print("size - получить размер очереди")
    print("show - показать содержимое очереди")
    print("выход - выйти из режима работы с очередью")
    
    for cmd in stdin:
        try:
            cmd = cmd.strip()
            
            if not cmd:
                continue
            
            if cmd.lower() == 'выход':
                print("Выход из режима очереди. Состояние сохранено.")
                break
            
            parts = cmd.split()
            command = parts[0].lower()
            
            if command == 'enqueue':
                if len(parts) < 2:
                    raise InvalidInputError("Укажите число для добавления (enqueue <число>)")
                try:
                    value = int(parts[1])
                    queue.enqueue(value)
                    print(f"Добавлено: {value}")
                except ValueError:
                    raise InvalidInputError("Необходимо целое число")
            
            elif command == 'dequeue':
                value = queue.dequeue()
                print(f"Удалено: {value}")
            
            elif command == 'front':
                value = queue.front()
                print(f"Первый элемент: {value}")
            
            elif command == 'size':
                size = queue.size()
                print(f"Размер очереди: {size}")
            
            elif command == 'show':
                if queue.is_empty():
                    raise QueueEmptyError("Очередь пустая")
                else:
                    print(f"Содержимое очереди (начало -> конец): {queue.items}")
            
            else:
                raise InvalidInputError(f"Неизвестная команда '{command}'")
        
        except QueueEmptyError:
            raise QueueEmptyError("Очередь пустая")
        except Exception as e:
            raise Exception(f"ERROR: Непредвиденная ошибка: {e}")
