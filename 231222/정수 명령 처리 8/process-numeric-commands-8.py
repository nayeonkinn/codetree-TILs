class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node

        else:
            self.head = new_node
            self.tail = new_node

        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        
        else:
            self.head = new_node
            self.tail = new_node

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print('List is empty')
        
        elif self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            return temp.data

    def pop_back(self):
        if self.tail == None:
            print('List is empty')
        
        elif self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        return 1 if self.node_num == 0 else 0

    def front(self):
        if self.head == None:
            print('List is empty')
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            print('List is empty')
        else:
            return self.tail.data


n = int(input())
dll = DLL()

for _ in range(n):
    command, *num = input().split()

    if command == 'push_front':
        dll.push_front(int(num[0]))

    elif command == 'push_back':
        dll.push_back(int(num[0]))

    elif command == 'pop_front':
        print(dll.pop_front())

    elif command == 'pop_back':
        print(dll.pop_back())

    elif command == 'size':
        print(dll.size())

    elif command == 'empty':
        print(dll.empty())

    elif command == 'front':
        print(dll.front())

    else:  # 'back'
        print(dll.back())