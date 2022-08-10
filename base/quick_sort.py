from array import array


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot, tail = arr[0], arr[1:]

    left_arr = [x for x in tail if x <= pivot]  # pivot보다 작거나 같은 원소들
    right_arr = [x for x in tail if x > pivot]  # pivot보다 큰 원소들

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


def quick_sort2(arr, left, right):
    if (left >= right):
        return

    pi = partition(arr, left, right)

    quick_sort2(arr, left, pi-1)
    quick_sort2(arr, pi+1, right)

def partition(arr, left, right):
    mid = (left + right) // 2
    swap(arr, left, mid)

    pivot = array[left]
    i, j = left, right

    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i < j and pivot >= arr[i]:
            i += 1
        swap(arr, i, j)

    arr[left] = arr[i]
    arr[i] = pivot
    return i

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
        