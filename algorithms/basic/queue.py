import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from list.linked_list import Node, List

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        num_nodes = 0
        k = self.head

        while k:
            if k is k.next:
                raise Exception('You have self referencing node')
            num_nodes += 1
            k = k.next

        return num_nodes

    def is_empty(self):
        return not bool(self.tail)

    def enqueue(self, item):
        if not self.tail:
            self.tail = item
            self.head = item
        else:
            self.tail.next = item
            self.tail = item

    def dequeue(self):
        if self.is_empty():
            raise KeyError("The stack is empty")

        item = self.head
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return item


if __name__ == '__main__':
    q = Queue()

    assert len(q) == 0
    assert q.is_empty()


    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)


    q.enqueue(a)
    assert not q.is_empty()
    assert len(q) == 1

    q.enqueue(b)
    q.enqueue(c)
    assert len(q) == 3
    
    val = q.dequeue()
    assert val is a
    
    val = q.dequeue()
    assert val is b
    assert len(q) == 1

    q.enqueue(d)
    q.enqueue(e)

    val = q.dequeue()
    assert val is c

    val = q.dequeue()
    assert val is d
    assert len(q) == 1

    val = q.dequeue()
    assert val is e
    assert len(q) == 0
    assert q.is_empty()
