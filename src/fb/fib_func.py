def fibonacci(n: int) -> int:
    try:
        # проверка на отрицательное число
        if n < 0:
            raise TypeError('Число Фибоначчи определен только для неотрицательных чисел')
        # базовые случаи
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # итеративное вычисление
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при вычислении числа Фибоначчи: {e}")