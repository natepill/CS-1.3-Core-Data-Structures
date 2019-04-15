from linkedlist import LinkedList, Node

class BinaryNode(Node):

    def __init__(self, data):
        super().__init__(data)
        self.prev = None


class DoublyLinkedList(LinkedList):

    def __init__(self):
        super().__init__(iterable=None)
        self.head = None
        self.tail = None
        self.size = 0



    # def 
