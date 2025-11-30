def radix_sort(a: list[int], base: int = 10) -> list[int]:
    # сортирует массив методом поразрядной сортировки
    if not a:
        return []
    
    arr = a.copy()
    max_val = max(arr)
    
    # обрабатываем каждый разряд
    exp = 1
    while max_val // exp > 0:
        # сортировка подсчетом для текущего разряда
        output = [0] * len(arr)
        count = [0] * base
        
        # подсчитываем количество элементов для каждой цифры
        for num in arr:
            index = (num // exp) % base
            count[index] += 1
        
        # вычисляем позиции элементов
        for i in range(1, base):
            count[i] += count[i - 1]
        
        # строим выходной массив
        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] // exp) % base
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        
        arr = output
        exp *= base
    
    return arr