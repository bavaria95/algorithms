import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from list.linked_list import Node, List

class Stack:
    def __init__(self):
        self.top = None

    def __len__(self):
        num_nodes = 0
        k = self.top

        while k:
            num_nodes += 1
            k = k.next

        return num_nodes

    def push(self, item):
        item.next = self.top
        self.top = item

    def pop(self):
        if not self.top:
            raise KeyError("The stack is empty")

        popped_node = self.top
        self.top = self.top.next

        return popped_node

    def is_empty(self):
        return not bool(self.top)

    def peek(self):
        return self.top


if __name__ == '__main__':
    s = Stack()

    assert len(s) == 0
    assert s.is_empty()

    s.push(Node(1))
    s.push(Node(2))
    s.push(Node(3))

    assert len(s) == 3
    assert not s.is_empty()

    assert s.peek().value == 3

    assert s.pop().value == 3
    assert len(s) == 2
    assert s.peek().value == 2

    s.pop()
    s.pop()

    assert s.is_empty()
