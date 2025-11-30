def fibonacci_recursive(n: int) -> int:
    try:
        # проверка на отрицательное число
        if n < 0:
            raise TypeError('Число Фибоначчи определен только для неотрицательных чисел')
        # базовые случаи рекурсии
        if n == 0:
            return 0
        if n == 1:
            return 1
        # рекурсивный вызов
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при вычислении числа Фибоначчи рекурсивно: {e}")