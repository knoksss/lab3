def heapify(lst, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # проверяем левый дочерний элемент
        if left < n and lst[left] > lst[largest]:
            largest = left
        
        # проверяем правый дочерний элемент
        if right < n and lst[right] > lst[largest]:
            largest = right
        
        # если наибольший элемент не корень
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            # рекурсивно применяем heapify
            heapify(lst, n, largest)

            
def heap_sort(a: list[int]) -> list[int]:
    # сортирует массив методом пирамидальной сортировки
    if not a:
        return []
    arr = a.copy()    

    n = len(arr)
    # построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # перемещаем текущий корень в конец
        arr[i], arr[0] = arr[0], arr[i]
        # восстанавливаем heap для оставшихся элементов
        heapify(arr, i, 0)
    
    return arr
