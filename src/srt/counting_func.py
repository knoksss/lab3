def counting_sort(a: list[int]) -> list[int] :
    # сортирует массив целых чисел методом подсчета
    if not a:
        return []
    
    # находим минимальное и максимальное значения
    min_val = min(a)
    max_val = max(a)
    
    # создаем массив для подсчета вхождений
    count = [0] * (max_val - min_val + 1)
    
    # подсчитываем количество каждого элемента
    for num in a:
        count[num - min_val] += 1
    
    # формируем отсортированный результат
    result = []
    for i, cnt in enumerate(count):
        result.extend([i + min_val] * cnt)
    
    return result