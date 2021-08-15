#####
# Linked List
#####

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # head will contains first Node

    def print(self):
        printval = self.head  # printval will be type Node
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insertAtBeginning(self, Node):
        Node.next = self.head
        self.head = Node

    def insertAtEnd(self, Node):
        if self.head is None:
            self.head = Node
        else:
            itr = self.head
            while itr is not None:
                if itr.next is None:
                    itr.next = Node
                    Node.next = None
                itr = itr.next

    def get_length(self):
        if self.head is None:
            return 0
        else:
            itr = self.head
            counter = 0
            while itr is not None:
                counter += 1
                itr = itr.next
            return counter

    def insertAt(self, index, Node):
        if index < 0 or index >= self.get_length():
            raise Exception("index out of bounds")
        if index == 0:
            self.insertAtBeginning(Node)
        if index == self.get_length()-1:
            self.insertAtEnd(Node)
        else:
            itr = self.head
            counter = 0
            while self.head is not None:
                if counter == index - 1:
                    ## prev node = node @ index -1
                    Node.next = itr.next
                    itr.next = Node
                    break
                counter += 1
                itr = itr.next

    def removeAt(self, index):
        if index < 0 and index >= self.get_length():
            raise Exception("index out of bounds")
        else:
            itr = self.head
            counter = 0
            while self.head is not None:
                if counter == index - 1:
                    ## prev node = node @ index -1
                    itr.next = itr.next.next
                    break
                counter += 1
                itr = itr.next


llist = LinkedList()
n1 = Node(10)
llist.head = n1
n2 = Node(18)
llist.head.next = n2  # llist.head = first Node
n3 = Node(21)
n2.next = n3

llist.print()
print("-" * 100)
llist.insertAtBeginning(Node(100))
llist.insertAtEnd(Node(1000))
llist.print()
print("length:", llist.get_length())
print("-" * 100)
print("inserting element at index 2")
llist.insertAt(2, Node("middle"))
llist.print()
print("-" * 100)
print("removing element at index 3")
llist.removeAt(3)
llist.print()
