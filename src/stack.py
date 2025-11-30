from sys import stdin
from src.stc.stack_func import Stack
from src.errors import InvalidInputError, StackEmptyError


def stack_interactive(stack: Stack):
    print("Доступные команды:")
    print("push <число> - добавить элемент")
    print("pop - удалить верхний элемент")
    print("peek - посмотреть верхний элемент")
    print("min - получить минимальный элемент")
    print("size - получить размер стека")
    print("show - показать содержимое стека")
    print("выход - выйти из режима работы со стеком")
    
    for cmd in stdin:
        try:
            cmd = cmd.strip()
            
            if not cmd:
                continue
            
            if cmd.lower() == 'выход':
                print("Выход из режима стека. Состояние сохранено.")
                break
            
            parts = cmd.split()
            command = parts[0].lower()
            
            if command == 'push':
                if len(parts) < 2:
                    raise InvalidInputError("ERROR: Укажите число для добавления (push <число>)")
                try:
                    value = int(parts[1])
                    stack.push(value)
                    print(f"Добавлено: {value}")
                except ValueError:
                    raise InvalidInputError("ERROR: Необходимо целое число")
            
            elif command == 'pop':
                value = stack.pop()
                print(f"Удалено: {value}")
            
            elif command == 'peek':
                value = stack.peek()
                print(f"Верхний элемент: {value}")
            
            elif command == 'min':
                value = stack.min()
                print(f"Минимальный элемент: {value}")
            
            elif command == 'size':
                size = stack.size()
                print(f"Размер стека: {size}")
            
            elif command == 'show':
                if stack.is_empty():
                    raise StackEmptyError("Стек пустой")
                else:
                    print(f"Содержимое стека (снизу вверх): {stack.items}")
            
            else:
                raise InvalidInputError(f"ERROR: Неизвестная команда '{command}'")
        
        except StackEmptyError:
            raise StackEmptyError("Стек пустой")
        except Exception:
            raise Exception("ERROR: Непредвиденная ошибка")
