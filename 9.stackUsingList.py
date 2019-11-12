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


def main():
    S1 = Stack()
    print('a.push \nb.pop \nc.done')

    while 1:
        i = input('Enter option: ')
        if i == 'a':
            n = int(input('Enter No: '))
            S1.push(n)
        elif i == 'b':
            poped = S1.pop()
            print(f'poped element is: {poped}')
        else:
            break



if __name__ == '__main__':
        main()