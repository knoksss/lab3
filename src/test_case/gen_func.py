import random
from src.errors import InvalidInputError


def rand_int_array(n: int, lo: int, hi: int, seed: int | None = None) -> list[int]:
    # генерирует массив случайных целых чисел
    if seed is not None:
        random.seed(seed)
    
    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, seed: int | None = None) -> list[int]:
    # генерирует почти отсортированный массив с заданным количеством перестановок
    if seed is not None:
        random.seed(seed)
    
    # создаём отсортированный массив
    arr = list(range(n))

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(n: int, k_unique: int = 5, seed: int | None = None) -> list[int]:
    # генерирует массив с большим количеством дубликатов
    if seed is not None:
        random.seed(seed)
    
    # генерируем уникальные значения
    unique_values = [random.randint(0, 100) for _ in range(k_unique)]
    
    # заполняем массив случайным выбором из уникальных значений
    return [random.choice(unique_values) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    # генерирует массив, отсортированный в обратном порядке
    return list(range(n, 0, -1))


def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, seed: int | None = None) -> list[float]:
    # генерирует массив случайных вещественных чисел
    if seed is not None:
        random.seed(seed)
    
    return [random.uniform(lo, hi) for _ in range(n)]


def test():
    # интерактивная генерация тест-кейсов для тестирования алгоритмов
    print("Генерация тест-кейсов\n")
    print("Выберите тип генерации:")
    print("1. rand_int_array - случайный массив целых чисел")
    print("2. nearly_sorted - почти отсортированный массив")
    print("3. many_duplicates - массив с дубликатами")
    print("4. reverse_sorted - обратно отсортированный массив")
    print("5. rand_float_array - массив случайных float чисел")
    
    choice = input("Введите номер: ").strip()
    
    try:
        if choice == '1':
            n = int(input("Количество элементов (n): "))
            lo = int(input("Минимальное значение (lo): "))
            hi = int(input("Максимальное значение (hi): "))
            seed = None
            
            result = rand_int_array(n, lo, hi, seed)
            print(f"Результат: {result}")
            
        elif choice == '2':
            n = int(input("Количество элементов (n): "))
            swaps = int(input("Количество перестановок (swaps): "))
            seed = None
            
            result = nearly_sorted(n, swaps, seed)
            print(f"Результат: {result}")
            
        elif choice == '3':
            n = int(input("Количество элементов (n): "))
            k_unique_input = input("Количество уникальных значений (Enter для 5): ").strip()
            k_unique = int(k_unique_input) if k_unique_input else 5
            seed = None
            
            result = many_duplicates(n, k_unique, seed)
            print(f"Результат: {result}")
            
        elif choice == '4':
            n = int(input("Количество элементов (n): "))
            
            result = reverse_sorted(n)
            print(f"Результат: {result}")
            
        elif choice == '5':
            n = int(input("Количество элементов (n): "))
            lo = float(input("Минимальное значение (lo, Enter для 0.0): ") or "0.0")
            hi = float(input("Максимальное значение (hi, Enter для 1.0): ") or "1.0")
            seed = None
            
            result = rand_float_array(n, lo, hi, seed)
            print(f"Результат: {result}")
            
        else:
            raise InvalidInputError("Неизвестная команда")
            
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при обработке в программе: {e}")