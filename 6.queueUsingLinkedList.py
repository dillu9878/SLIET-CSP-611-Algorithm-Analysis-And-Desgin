class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def add_to_end(self, data):
        temp1 = Node(data)

        if self.start is None:
            self.start = temp1
        else:
            temp2 = self.start
            while temp2.next:
                temp2 = temp2.next
            temp2.next = temp1

    def delete_from_start(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            data = self.start.data
            self.start = None
            return data
        else:
            data = self.start.data
            self.start = self.start.next
            return data


class Queue:
    def __init__(self):
        self.L1 = LinkedList()

    def enqueue(self, data):
        self.L1.add_to_end(data)

    def dequeue(self):
        d = self.L1.delete_from_start()
        return d


def main():
    Q1 = Queue()
    print('1.Enqueue \n2.Dequeue \n3.Done')
    flag = 1
    while flag:
        inp = input('Enter Your Option: ')
        if inp == '1':
            data = input('Enter data: ')
            Q1.enqueue(data)
        elif inp == '2':
            data = Q1.dequeue()
            print('Dequeued Data is: ', data)
        else:
            flag = 0


if __name__ == '__main__':
    main()