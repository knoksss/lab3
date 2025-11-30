def factorial_recursive(n: int) -> int:
    try:
        # проверка на отрицательное число
        if n < 0:
            raise TypeError('Факториал определен только для неотрицательных чисел')
        # базовый случай рекурсии
        if n == 0 or n == 1:
            return 1
        # рекурсивный вызов
        return n * factorial_recursive(n - 1)
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при вычислении факториала рекурсивно: {e}")