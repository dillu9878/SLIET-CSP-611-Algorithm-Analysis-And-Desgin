def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def main():
    l = list(map(int, input('Enter array: ').split()))
    print('Sorted  List: ', selectionSort(l))


if __name__ == '__main__':
    main()