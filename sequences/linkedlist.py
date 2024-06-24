from .sequencebase import SequenceBase
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList(SequenceBase):
    def __init__(self):
        self.head = None
        self.__count = 0
    def to_list(self):
        l = []
        current = self.head
        while current:
            l.append(current.data)
            current = current.next
        return l
    def append(self, data):
        """Append an element to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.__count += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.__count += 1

    def iter_delete(self, isSameTarget):
        if not self.head:
            return

        if isSameTarget(self.head.data):
            self.head = self.head.next
            return

        current = self.head
        while current.next and (not isSameTarget(current.next.data)):
            current = current.next

        if current.next:
            current.next = current.next.next

    def length(self):
        return self.__count