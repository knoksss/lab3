def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    # сортирует массив методом блочной сортировки (bucket sort)
    if not a:
        return []
    arr = a.copy()
    # нормализация к диапазону [0, 1)
    min_val = min(arr)
    max_val = max(arr)
    
    if min_val < 0 or max_val >= 1:
        # нормализация значений
        normalized = []
        for num in arr:
            normalized_num = (num - min_val) / (max_val - min_val + 1e-10)
            normalized.append(normalized_num)
        arr = normalized

    n = len(arr)
    if buckets is None:
        buckets = n
    
    bucket_list = [[] for _ in range(buckets)] # создание ведер
    
    # распределение элементов по ведрам
    for num in arr:
        index = int(num * buckets)
        if index == buckets:  # Обработка граничного случая для 1.0
            index = buckets - 1
        bucket_list[index].append(num)
    
    # сортировка каждого ведра (используем быструю сортировку)
    for i in range(buckets):
        bucket_list[i] = simple_sort(bucket_list[i])
    
    # сборка результата
    result = []
    for bucket in bucket_list:
        result.extend(bucket)
    
    # денормализация
    if min_val < 0 or max_val >= 1:
        result = [num * (max_val - min_val) + min_val for num in result]
    
    return result


def simple_sort(arr: list[float]) -> list[float]:
    # простая пузырьковая сортировка для сортировки содержимого ведер
    n = len(arr)
    
    for i in range(n):
        # проходим по массиву, сравнивая соседние элементы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # меняем местами, если текущий элемент больше следующего
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
