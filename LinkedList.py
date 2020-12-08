class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.head.next = None
        self.head.prev = None
        self.size = 1

    def addNode(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.size = 1
            return
        newNode = Node(value)
        newNode.prev = self.head
        self.head.next = newNode
        self.head = newNode
        self.size += 1

    def printList(self):

        while self.head.prev is not None:
            print(self.head.value)
            self.head = self.head.prev
            # if self.head.next is not None :
        print(self.head.value)

    def removeLastNode(self):
        prev = self.head.prev
        self.head = prev
        self.size -= 1

    def removeNode(self, index):
        head = self.head
        size = 0
        if index < 0 or index >= self.size:
            return
        if index == (self.size - 1):
            self.removeLastNode()
            return
        if index == 0:
            while self.head.prev is not None:
                self.head = self.head.prev
            self.head.next.prev = None
            self.head = None
            self.head = head
            self.size -= 1
            return
        while (size != (self.size - index - 1)):
            size += 1
            self.head = self.head.prev
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = head
        self.size -= 1

    def addNodeAt(self, value, index):
        if index < 0 or index >= (self.size):
            return
        head = self.head
        newNode = Node(value);
        size = 0
        while (size != (self.size - index)):
            size += 1
            self.head = self.head.prev
        next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head

        newNode.next = next
        next.prev = newNode
        # print(cur.next.value)
        self.head = head
        self.size += 1
