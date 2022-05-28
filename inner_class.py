
# outer class
class LinkedList:

    # inner class
    class Node:
        def __init__(self, val: int = -1, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

        def __str__(self):
            return f'({self.val})'

    def __init__(self):
        self.__head = self.Node()
        self.__tail = self.Node()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    @property
    def head(self):
        return self.__head.next if self.__head.next is not self.__tail else None

    @property
    def tail(self):
        return self.__tail.prev if self.__tail.prev is not self.__head else None

    def append(self, val: int):
        prev = self.__tail.prev
        node = self.Node(val)
        prev.next = node
        node.prev = prev
        node.next = self.__tail
        self.__tail.prev = node

    def __str__(self):
        l = []
        p = self.head
        while p != self.__tail:
            l.append(p.__str__())
            p = p.next
        return "->".join(l)


l = LinkedList()
print(l.head, l.tail)
l.append(1)
l.append(2)
l.append(3)

print(l.head, l.tail)
print(l)
