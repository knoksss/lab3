def quick_sort(a: list[int]) -> list[int]:
    # сортирует массив методом быстрой сортировки
    if not a:
        return []
    
    arr = a.copy()
    

    def _quick_sort(lst, low, high):
        # рекурсивная функция быстрой сортировки
        if low < high:
            # получаем индекс опорного элемента
            pi = _partition(lst, low, high)
            # сортируем левую часть
            _quick_sort(lst, low, pi - 1)
            # сортируем правую часть
            _quick_sort(lst, pi + 1, high)
    

    def _partition(lst, low, high):
        # разделяет массив относительно опорного элемента
        pivot = lst[high]
        i = low - 1
        # перемещаем элементы меньше опорного влево
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        # ставим опорный элемент на правильное место
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1
    
    _quick_sort(arr, 0, len(arr) - 1)
    return arr