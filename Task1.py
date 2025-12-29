import random
import timeit

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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else []
            merged.append(merge(l1, l2))

        lists = merged

    return lists[0]

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


#Test Data
def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]


# Benchmark
def benchmark():
    sizes = [100, 1_000, 5_000]

    for size in sizes:
        data = generate_data(size)

        print(f"\nArray size: {size}")

        t_insertion = timeit.timeit(
            lambda: insertion_sort(data), number=1
        )

        t_merge = timeit.timeit(
            lambda: merge_sort(data), number=1
        )

        t_timsort = timeit.timeit(
            lambda: sorted(data), number=1
        )

        print(f"Insertion Sort: {t_insertion:.6f} sec")
        print(f"Merge Sort:     {t_merge:.6f} sec")
        print(f"Timsort:        {t_timsort:.6f} sec")


if __name__ == "__main__":
    benchmark()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Відсортований список:", merge_k_lists(lists))






