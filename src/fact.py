from src.fac.fact_func import factorial
from src.fac.fact_r_func import factorial_recursive
from src.errors import FlagError


def fact():
    print('Есть возможность посчитать итеративно и рекурсивно.\n' \
    'Для рекурсивного введите -r, для итеративного -i, а после введите число.')
    cmd = input().split()
    try:
        if cmd[0] == '-r':
            result = factorial_recursive(int(cmd[1]))
            print(f'Результат: {result}')
            return result
        elif cmd[0] == '-i':
            result = factorial(int(cmd[1]))
            print(f'Результат: {result}')
            return result
        else:
            raise FlagError("Неизвестный флаг")
        
    except Exception as e:
        raise Exception(f"ERROR: Непредвиденная ошибка: {e}")