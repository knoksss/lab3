from src.srt.bubble_func import bubble_sort
from src.srt.bucket_func import bucket_sort
from src.srt.counting_func import counting_sort
from src.srt.heap_func import heap_sort
from src.srt.quick_func import quick_sort
from src.srt.radix_func import radix_sort
from src.test_case.gen_func import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
import pytest


def test_bubble_sort_basic():
    assert bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_single_element():
    assert bubble_sort([42]) == [42]
    assert bubble_sort([-1]) == [-1]


def test_bubble_sort_negative_numbers():
    assert bubble_sort([-3, -1, -2]) == [-3, -2, -1]
    assert bubble_sort([0, -5, 5]) == [-5, 0, 5]


def test_bucket_sort_basic():
    assert bucket_sort([0.1, 0.5, 0.3, 0.8, 0.2]) == [0.1, 0.2, 0.3, 0.5, 0.8]
    assert bucket_sort([0.9, 0.1, 0.5]) == [0.1, 0.5, 0.9]
    assert bucket_sort([0.1, 0.2, 0.3]) == [0.1, 0.2, 0.3]


def test_bucket_sort_empty():
    assert bucket_sort([]) == []


def test_bucket_sort_single_element():
    assert bucket_sort([42]) == [42]
    assert bucket_sort([-1]) == [-1]


def test_counting_sort_basic():
    assert counting_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_counting_sort_empty():
    assert counting_sort([]) == []


def test_counting_sort_single_element():
    assert counting_sort([42]) == [42]
    assert counting_sort([-1]) == [-1]


def test_counting_sort_negative_numbers():
    assert counting_sort([-3, -1, -2]) == [-3, -2, -1]
    assert counting_sort([0, -5, 5]) == [-5, 0, 5]


def test_heap_sort_basic():
    assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_heap_sort_empty():
    assert heap_sort([]) == []


def test_heap_sort_single_element():
    assert heap_sort([42]) == [42]
    assert heap_sort([-1]) == [-1]


def test_heap_sort_negative_numbers():
    assert heap_sort([-3, -1, -2]) == [-3, -2, -1]
    assert heap_sort([0, -5, 5]) == [-5, 0, 5]


def test_quick_sort_basic():
    assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single_element():
    assert quick_sort([42]) == [42]
    assert quick_sort([-1]) == [-1]


def test_quick_sort_negative_numbers():
    assert quick_sort([-3, -1, -2]) == [-3, -2, -1]
    assert quick_sort([0, -5, 5]) == [-5, 0, 5]


def test_radix_sort_basic():
    assert radix_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_radix_sort_empty():
    assert radix_sort([]) == []


def test_radix_sort_single_element():
    assert radix_sort([42]) == [42]
    assert radix_sort([-1]) == [-1]


def test_basic_generation():
        result = rand_int_array(5, 1, 10)
        assert len(result) == 5
        assert all(isinstance(x, int) for x in result)
        assert all(1 <= x <= 10 for x in result)


def test_basic_generation():
        n = 10
        swaps = 3
        result = nearly_sorted(n, swaps)
        
        assert len(result) == n
        assert set(result) == set(range(n))

    
def test_basic_generation():
        result = many_duplicates(10, 3, seed=42)
        assert len(result) == 10
        assert len(set(result)) <= 3

    
def test_basic_generation():
        result = reverse_sorted(5)
        assert result == [5, 4, 3, 2, 1]


def test_basic_generation():
        result = rand_float_array(5, 0.0, 1.0)
        assert len(result) == 5
        assert all(isinstance(x, float) for x in result)
        assert all(0.0 <= x <= 1.0 for x in result)


def test_generators_correct_len():
        generators = [
            lambda: rand_int_array(10, 1, 100),
            lambda: nearly_sorted(10, 3),
            lambda: many_duplicates(10, 3),
            lambda: reverse_sorted(10),
            lambda: rand_float_array(10, 0.0, 1.0)
        ]
        
        for generator in generators:
            result = generator()
            assert len(result) == 10