class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

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

    def add_to_start(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start = temp


class Stack:
    def __init__(self):
        self.L1 = LinkedList()

    def push(self, data):
        self.L1.add_to_start(data)

    def pop(self):
        data = self.L1.delete_from_start()
        return data


def main():
    S1 = Stack()
    print('1.push \n2.pop \n3.Done')
    flag = 1
    while flag:
        inp = input('Enter Your Option: ')
        if inp == '1':
            data = input('Enter data: ')
            S1.push(data)
        elif inp == '2':
            data = S1.pop()
            print('poped Data is: ', data)
        else:
            flag = 0


if __name__ == '__main__':
    main()