class Stack:
    def __init__(self):
        self.top = None
        self.arr = []

    def push(self, data):
        if self.top is None:
            self.arr.append(data)
            self.top = 1
        else:
            self.arr.append(data)
            self.top += 1

    def pop(self):
        if self.top is None:
            return "Stack is Empty"
        else:
            d = self.arr.pop()
            if len(self.arr) == 0:
                self.top = None
            return d



class Queue:
    def __init__(self):
        self.front =  None
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
    S1 = Stack()
    S1.push(5)
    S1.push(10)
    print(S1.pop())
    print(S1.pop())
    print(S1.pop())
    Q1 = Queue()
    Q1.enqueue(5)
    Q1.enqueue(10)
    print(Q1.dequeue())
    print(Q1.dequeue())
    print(Q1.dequeue())


if __name__ == '__main__':
        main()