def max_heap(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2
    Max = i
    if l < n and arr[l] > arr[Max]:
        Max = l
    if r < n and arr[r] > arr[Max]:
        Max = r

    if Max != i:
        arr[i], arr[Max] = arr[Max], arr[i]
        max_heap(arr, n, Max)
    return arr


def build_max_heap(arr):
    l = len(arr)
    for i in range(l, -1, -1):
        arr = max_heap(arr,l, i)
    return arr


def heap_sort(arr):
    arr = build_max_heap(arr)
    print(arr, '****')
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr = max_heap(arr, i,  0)
    print(arr)
    return arr


if __name__ == '__main__':
    List = list(map(int, input('Enter Element of List: ').split()))
    arr = heap_sort(List)
    print('Sorted List:', arr)



