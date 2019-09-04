def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    l = list(map(int, input('Enter element of list: ').split()))
    l = insertion_sort(l)
    print('Sorted list is: ', l)


if __name__ == '__main__':
    main()

