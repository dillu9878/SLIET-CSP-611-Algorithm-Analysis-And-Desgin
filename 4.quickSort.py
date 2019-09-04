class QuickSort:

    def quickSort(self,l: list):
        if len(l) <= 1:
            return l
        pivot = l[-1] ##last element of list
        l1, l2, l3 = [], [], []
        for i in l:
            if i < pivot:
                l1.append(i)
            elif i > pivot:
                l2.append(i)
            else:
                l3.append(i)
        return self.quickSort(l1) + l3 + self.quickSort(l2)


def main():
    List = list(map(int,input('Enter list element:').split()))
    S = QuickSort()
    print('sorted list is:{}'.format((S.quickSort(List))))


if __name__ == '__main__':
    main()