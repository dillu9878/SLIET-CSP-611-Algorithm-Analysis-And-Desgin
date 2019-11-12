class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.arr = []

    def enqueue(self, data):
        if self.rear is None:
            self.rear = 1
            self.front = 1
        else:
            self.rear += 1
        self.arr.append(data)

    def dequeue(self):
        if self.front is None:
            return 'Queue is Empty'
        else:
            d = self.arr.pop(0)
            self.front += 1
            if self.front >self.rear:
                self.front = None
                self.rear = None

            return d


def main():
    Q1 = Queue()
    print('a.enqueue \nb.dequeue \nc.quit')


    while 1:
        i = input('Enter choice: ')
        if i == '1':
            n = int(input('Enter Number: '))
            Q1.enqueue(n)
        elif i == '2':
            poped = Q1.dequeue()
            print(f'dequeued element is: {poped}')
        else:
            break


if __name__ == '__main__':
    main()