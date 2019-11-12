from random import randint
from time import time


def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return None


def binary_search(arr, lower, upper, num):
    mid = (lower+upper)//2
    if arr[mid] == num:
        return mid
    elif arr[mid] <= num:
        lower = mid + 1
        return binary_search(arr, lower, upper, num)
    elif arr[mid] > num:
        upper = mid - 1
        return binary_search(arr, lower, upper, num)
    else:
        return None


def arr_generator(size):
    arr = [randint(1,10)]
    for i in range(size-1):
        arr.append(arr[-1] + randint(1,10))
    return arr


def main():
    for _ in range(int(input('Enter the number of comp, Do you want: '))):
        size = int(input('Enter size of sorted array: '))
        arr = arr_generator(size)
        num = arr[randint(1, size)]
        #print(arr)
        t1 = time()
        print('Element {} found in list at index {} using linear search'.format(num, linear_search(arr, num)))
        t2 = time()
        print('Element {} found in list at index {} using binary search'.format(num, binary_search(arr, 0, size, num)))
        t3 = time()
        l_t, b_t = t2-t1, t3 - t2
        print('Linear search took about {} sec'.format(l_t))
        print('Binary search took about {} sec'.format(b_t))


if __name__ == '__main__':
    main()
