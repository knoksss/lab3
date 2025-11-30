from src.srt.bubble_func import bubble_sort
from src.srt.bucket_func import bucket_sort
from src.srt.counting_func import counting_sort
from src.srt.heap_func import heap_sort
from src.srt.quick_func import quick_sort
from src.srt.radix_func import radix_sort
from src.errors import InvalidInputError


def sort():
    print('Есть возможность использовать такие сортировки:\n' \
    '1. Bubble/Пузырьковая\n' \
    '2. Bucket\n' \
    '3. Counting/Подсчётом\n' \
    '4. Heap\n' \
    '5. Quick/Быстрая\n' \
    '6. Radix\n' \
    'Для вызова одной из них напишите её название и цифры для сортировки.')

    cmd = input().split()
    try:
        numbers = [int(x) for x in cmd[1:]]
        if cmd[0].lower() in ['bubble', 'пузырьковая']:
            result = bubble_sort(numbers)
        elif cmd[0].lower() in ['bucket']:
            result = bucket_sort(numbers)
        elif cmd[0].lower() in ['heap']:
            result = heap_sort(numbers)
        elif cmd[0].lower() in ['counting', 'подсчётом']:
            result = counting_sort(numbers)
        elif cmd[0].lower() in ['radix']:
            result = radix_sort(numbers)
        elif cmd[0].lower() in ['quick', 'быстрая']:
            result = quick_sort(numbers)
        else:
            raise InvalidInputError("Неизвестная команда")
        
        print(f'Отсортированный массив: {result}')
        return result
        
    except Exception as e:
        raise Exception(f"ERROR: Ошибка при обработке в программе: {e}")