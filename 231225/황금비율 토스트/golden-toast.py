class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push(self, iterator, new_data):
        if iterator == self.head:
            new_node = Node(new_data)
            new_node.next = self.head

            self.head.prev = new_node
            self.head = new_node

        elif iterator == self.tail:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            new_node.next = self.tail

            self.tail.prev.next = new_node
            self.tail.prev = new_node

        else:
            new_node = Node(new_data)
            new_node.prev = iterator.prev
            new_node.next = iterator

            iterator.prev.next = new_node
            iterator.prev = new_node
    
    def erase(self, iterator):
        next_node = iterator.next

        if iterator == self.head:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

        else:
            iterator.prev.next = iterator.next
            iterator.next.prev = iterator.prev
            iterator.prev = None
            iterator.next = None
        
        return next_node
    
    def begin(self):
        return self.head
    
    def end(self):
        return self.tail


n, m = map(int, input().split())

dll = DoublyLinkedList()
for i in input():
    dll.push(dll.end(), i)

it = dll.end()
for _ in range(m):
    code, *char = input().split()

    if code == 'L' and it.prev:
        it = it.prev

    elif code == 'R' and it.next:
        it = it.next

    elif code == 'D':
        it = dll.erase(it)

    else:  # 'P'
        dll.push(it, char[0])

it = dll.begin()
while it.next:
    print(it.data, end = '')
    it = it.next