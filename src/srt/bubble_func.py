def bubble_sort(a: list[int]) -> list[int]:
    # сортирует массив методом пузырьковой сортировки
    if not a:
        return []
    
    arr = a.copy()  # создаем копию, чтобы не изменять исходный массив
    n = len(arr)
    
    for i in range(n):
        # проходим по массиву, сравнивая соседние элементы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # меняем местами, если текущий элемент больше следующего
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
