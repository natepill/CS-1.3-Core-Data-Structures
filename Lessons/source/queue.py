#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.head is None

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) most of time """
        self.list.append(item)
        # TODO: Insert given item

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.list.is_empty():
            return None
        return self.list.head.data
        # TODO: Return front item, if any

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – make self.head.next = self.head """

        if self.list.is_empty():
            raise ValueError("List Empty")

        dequeued_value = self.list.head.data
        self.list.delete(dequeued_value)

        return dequeued_value

        # TODO: Remove and return front item, if any


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)
        # TODO: Count number of items

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O1 – Append in an dynamic array is constant time operation most of the time"""
        self.list.append(item)
        # TODO: Insert given item

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if not is_empty():
            return self.list[0]

        # TODO: Return front item, if any

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Array reallocate"""
        return self.list.pop(0)

        # TODO: Remove and return front item, if any


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
