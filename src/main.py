from sys import stdin
from src.fact import fact
from src.fib import fib
from src.sort import sort
from src.stc.stack_func import Stack
from src.que.queue_func import Queue
from src.stack import stack_interactive
from src.queue import queue_interactive
from src.test_case.gen_func import test
from src.benchmarks.bench_func import bench
from src.errors import InvalidInputError

print('Список команд для использования:\n' \
'1. Числа Фибоначчи (для использования напишите: fib)\n' \
'2. Факториал (исп.: fact)\n' \
'3. Сортировки (исп.: sort)\n' \
'4. Стек (исп.: stack)\n' \
'5. Очередь (исп.: queue)\n' \
'6. Генрация тест-кейсов (исп.: test)\n' \
'7. Бенчмарки (исп.: bench)\n' \
    'Для выхода напишите: "Стоп!"')

# переменные стека и очереди для сохранения состояния
global_stack = Stack()
global_queue = Queue()

for cmd in stdin:
    try:
        cmd = cmd.strip()
        if cmd.lower() in ['стоп!','стоп']:
            break
        if not cmd:
            print('Введите команду')
            continue

        if cmd == 'fib':
            fib()
        elif cmd == 'fact':
            fact()
        elif cmd == 'sort':
            sort()
        elif cmd == 'stack':
            stack_interactive(global_stack)

        elif cmd == 'queue':
            queue_interactive(global_queue)
            
        elif cmd == 'test':
            test()
        elif cmd == 'bench':
            bench()
        else:
            raise InvalidInputError("Неизвестная команда")
        
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при обработке в программе:{e}")