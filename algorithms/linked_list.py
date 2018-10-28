'''
    Simple implementation of Single-Linked List
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class List:
    def __init__(self):
        self.head = None

    def __repr__(self):
        s = '['
        k = self.head
        while k:
            if k.next:
                s += '%s, ' % k
            else:
                s += '%s' % k
            k = k.next
        s += ']'
        return s

    def add_first(self, node):
        if not self.head:
            self.head = node
            return self.head

        # supporting providing a chain of nodes
        k = node
        while k.next:
            k = k.next
        k.next = self.head

        self.head = node
        return self.head

    def remove_first(self):
        if self.head:
            self.head = self.head.next

        return self.head

    def add_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

        return new_node

    def remove_node(self, node):
        if self.head == node:
            self.head = node.next
            return self.head

        prev_node = None
        curr_node = self.head
        while curr_node and curr_node != node:
            prev_node = curr_node
            curr_node = curr_node.next

        if not curr_node:
            raise IndexError("Node %s isn't in the list" % node)

        prev_node.next = curr_node.next
        return curr_node.next


    def add_last(self, node):
        if not self.head:
            self.head = node
            return self.head

        k = self.head
        while k.next:
            k = k.next
        self.add_after(k, node)
        return node

    def remove_last(self):
        prev_node = None
        curr_node = self.head

        while curr_node:
            prev_node = curr_node
            curr_node = curr_node.next

        if not prev_node:
            return
        return self.remove_node(prev_node)


if __name__ == '__main__':
    l = List()

    for i in range(10):
        node = Node(i)
        l.add_first(node)
    print(l)

    l.remove_last()
    print(l)

    for i in range(9):
        l.remove_first()
    print(l)

