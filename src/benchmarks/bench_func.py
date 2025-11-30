import time
from typing import Callable, Dict, List
from src.srt.bubble_func import bubble_sort
from src.srt.bucket_func import bucket_sort
from src.srt.counting_func import counting_sort
from src.srt.heap_func import heap_sort
from src.srt.quick_func import quick_sort
from src.srt.radix_func import radix_sort


def timeit_once(func: Callable, *args, **kwargs) -> float:
    # измеряет время выполнения функции
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_sorts(
    arrays: Dict[str, List[int]], 
    algos: Dict[str, Callable], 
    callable: bool = True
) -> Dict[str, Dict[str, float]]:
    # выполняет бенчмарк алгоритмов сортировки
    results = {}

    print(f"{'Алгоритм':<20} {'Массив':<30} {'Время (сек)':<15}")
    
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        
        for array_name, array_data in arrays.items():
            # копируем массив для каждого теста
            test_array = array_data.copy()
            
            try:
                # измеряем время выполнения
                elapsed_time = timeit_once(algo_func, test_array)
                results[algo_name][array_name] = elapsed_time
                
                print(f"{algo_name:<20} {array_name:<30} {elapsed_time:.6f}")
                
            except Exception as e:
                print(f"{algo_name:<20} {array_name:<30} ERROR: {str(e)}")
                results[algo_name][array_name] = float('inf')

    print("Сводка результатов (среднее время по всем массивам):") # вывод сводки
    avg_times = {}
    for algo_name, algo_results in results.items():
        valid_times = [t for t in algo_results.values() if t != float('inf')]
        if valid_times:
            avg_times[algo_name] = sum(valid_times) / len(valid_times)
        else:
            avg_times[algo_name] = float('inf')
    
    # сортируем алгоритмы по среднему времени
    sorted_algos = sorted(avg_times.items(), key=lambda x: x[1])
    
    for i, (algo_name, avg_time) in enumerate(sorted_algos, 1):
        if avg_time == float('inf'):
            print(f"{i}. {algo_name:<20} ERROR")
        else:
            print(f"{i}. {algo_name:<20} {avg_time:.6f} сек")
    
    return results if callable else {}


def bench():
    """запускает интерактивный бенчмарк алгоритмов сортировки"""
    from src.test_case.gen_func import (
        rand_int_array, 
        nearly_sorted, 
        many_duplicates, 
        reverse_sorted
    )
    
    print("Бенчмарк алгоритмов сортировки")
    print("Настройка параметров тестирования:")
    
    try:
        # получаем размер массивов
        size_input = input("Размер массивов (Enter для 1000): ").strip()
        size = int(size_input) if size_input else 1000
        
        test_arrays = {
            "Случайный массив": rand_int_array(size, 0, size * 10, seed=42),
            "Почти отсортированный": nearly_sorted(size, size // 20, seed=42),
            "Много дубликатов": many_duplicates(size, k_unique=10, seed=42),
            "Обратно отсортированный": reverse_sorted(size),
            "Уже отсортированный": list(range(size)),
        }
        # определяем алгоритмы для тестирования
        sorting_algos = {
            "Bubble Sort": bubble_sort,
            "Bucket Sort": lambda arr: bucket_sort([float(x) for x in arr]),
            "Counting Sort": counting_sort,
            "Heap Sort": heap_sort,
            "Quick Sort": quick_sort,
            "Radix Sort": radix_sort,
        }
        # запускаем бенчмарки
        print()
        benchmark_sorts(test_arrays, sorting_algos, callable=False)
        
    except ValueError:
        print(f"ERROR: Неверный ввод")
    except Exception:
        print(f"ERROR: Ошибка при выполнении бенчмарка")


if __name__ == "__main__":
    bench()
