import random
import time
import sys

# Increase recursion depth for larger datasets
sys.setrecursionlimit(20000)

# -----------------------------
# INSERTION SORT
# -----------------------------
def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# -----------------------------
# MERGE SORT
# -----------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------
# QUICK SORT
# -----------------------------
def quick_sort(arr):
    a = arr.copy()
    _quick_sort(a, 0, len(a) - 1)
    return a


def _quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    # Use middle element as pivot to avoid worst-case on sorted arrays
    mid = (low + high) // 2

    # Swap middle with last
    arr[mid], arr[high] = arr[high], arr[mid]

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# -----------------------------
# BENCHMARK FUNCTION
# -----------------------------
def benchmark(sort_function, dataset):
    data_copy = dataset.copy()  # Prevent original dataset from changing

    start = time.perf_counter()

    sort_function(data_copy)

    end = time.perf_counter()

    return end - start


# -----------------------------
# DATASET GENERATION
# -----------------------------
sizes = [1000, 5000, 10000]

for size in sizes:
    print("\n" + "=" * 50)
    print(f"DATASET SIZE: {size}")
    print("=" * 50)

    # Random dataset
    random_data = [random.randint(1, 100000) for _ in range(size)]

    # Sorted dataset
    sorted_data = sorted(random_data)

    # Reverse sorted dataset
    reverse_data = sorted(random_data, reverse=True)

    datasets = {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reverse": reverse_data
    }

    for dtype, data in datasets.items():
        print(f"\n{dtype} Data:")

        insertion_time = benchmark(insertion_sort, data)
        merge_time = benchmark(merge_sort, data)
        quick_time = benchmark(quick_sort, data)

        print(f"Insertion Sort: {insertion_time:.6f} seconds")
        print(f"Merge Sort:     {merge_time:.6f} seconds")
        print(f"Quick Sort:     {quick_time:.6f} seconds")