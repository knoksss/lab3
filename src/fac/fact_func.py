def factorial(n: int) -> int:
    try:
        # проверка на отрицательное число
        if n < 0:
            error = "Факториал определен только для неотрицательных чисел"
            raise TypeError(f'{error}')
        result = 1
        # вычисляем произведение всех чисел от 1 до n
        for i in range(1, n + 1):
            result *= i
        return result
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при вычислении факториала: {e}")