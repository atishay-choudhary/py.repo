print("Demo")


def quicksort(arr):
    """
    Sorts an array using the QuickSort algorithm.

    Time complexity: O(n log n) on average, O(n^2) in worst case
    Space complexity: O(log n) on average, O(n) in worst case

    :param arr: The array to be sorted
    :return: The sorted array
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def merge_sort(arr1, arr2):

    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        mid = len(arr) // 2
        l1 = mergesort(arr[:mid])
        l2 = mergesort(arr[mid:])
    return merge_sort(l1, l2)


def bubblesort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num]
