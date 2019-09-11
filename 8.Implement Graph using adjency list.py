class Graph:
    def __init__(self):
        self.node_list = []
        self.child_list = []

    def addNode(self, u):
        if u not in self.node_list:
            self.node_list.append(u)
        else:
            print()

    def deleteNode(self, u):
        if u in self.node_list:

            for i in range(len(self.child_list)):
                if u  in self.child_list[i]:
                    self.child_list[i].remove(u)

            self.node_list.remove(u)
            print('Node {} Deleted.'.format(u))
        else:
            print('Node {} not existed.'.format(u))

    def searchNode(self, u):
        if u in self.node_list:
            print('Node {} existed.'.format(u))

        else:
            print('Node {} not existed.')

    def addEdge(self, u, v):
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_list.append(v)
            self.child_list.append([v])
            print('({}, {})Edge is Added'.format(u, v))

        else:
            i = self.node_list.index(u)
            if v not in self.node_list:
                self.node_list.append(v)
            self.child_list[i].append(v)
            print('({}, {})Edge is Added'.format(u, v))

    def deleteEdge(self, u, v):
        if u in self.node_list:
            i = self.node_list.index(u)
            temp = self.child_list[i]

            if v in temp:
                if len(temp) == 1:
                    self.node_list.remove(u)
                    self.child_list.remove(temp)
                    print('({}, {})Edge is Deleted'.format(u, v))

                else:
                    self.child_list[i].remove(v)
                    print('({}, {})Edge is Deleted'.format(u, v))

            else:
                print('({}, {})Edge is Not Exist'.format(u, v))

        else:
            print('({}, {})Edge is Not Exist'.format(u, v))

    def searchEdge(self, u, v):
        if u in self.node_list:
            i = self.node_list.index(u)
            if v in self.child_list[i]:
                print('({}, {}) Edge is Existed'.format(u, v))

            else:
                print('({}, {}) Edge is Not Exist'.format(u, v))

        else:
            print('({}, {})Edge is Not Exist'.format(u, v))


def main():
    G1 = Graph()
    print('1.Add Node \n2.Delete Node \n3.Search Node \n4.Add Edge \n5.Delete Edge \n6.Search Edge \n7.Done')
    flag = 1
    while flag:
        inp = input('Enter Your Option: ')
        if inp == '1':
            u = int(input('Enter Node: '))
            G1.addNode(u)

        elif inp == '2':
            u = int(input('Enter Node: '))
            G1.deleteNode(u)

        elif inp == '3':
            u = int(input('Enter Node: '))
            G1.searchNode(u)

        elif inp == '4':
            u, v = map(int, input('Enter u v: ').split())
            G1.addEdge(u, v)

        elif inp == '5':
            u, v = map(int, input('Enter u v: ').split())
            G1.deleteEdge(u, v)

        elif inp == '6':
            (u, v) = map(int, input('Enter u v: ').split())
            G1.searchEdge(u, v)

        else:
            flag = 0


if __name__ == '__main__':
    main()