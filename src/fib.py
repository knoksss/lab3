from src.fb.fib_func import fibonacci
from src.fb.fib_r_func import fibonacci_recursive
from src.errors import FlagError


def fib():
    print('Есть возможность посчитать итеративно и рекурсивно.\n' \
    'Для рекурсивного введите -r, для итеративного -i, а после введите число.')
    cmd = input().split()
    try:
        if cmd[0] == '-r':
            result = fibonacci_recursive(int(cmd[1]))
            print(f'Результат: {result}')
            return result
        elif cmd[0] == '-i':
            result = fibonacci(int(cmd[1]))
            print(f'Результат: {result}')
            return result
        else:
            raise FlagError("Неизвестный флаг")
        
    except Exception as e:
        raise Exception(f"ERROR: Непредвиденная ошибка: {e}")