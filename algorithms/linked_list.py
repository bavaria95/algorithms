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

    def __len__(self):
        num_nodes = 0
        k = self.head
        while k:
            num_nodes += 1
            k = k.next

        return num_nodes

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration

        prev_node = self.current
        self.current = self.current.next
        return prev_node

    def __getitem__(self, key):
        '''
        Getting element in the list by key-th index
        '''
        if not isinstance(key, int):
            raise TypeError("Key should be integer")

        if key < 0:
            raise KeyError("Key can't be negative")

        if not self.head:
            raise KeyError("List doesn't have node by key %s" % key)

        k = self.head
        for i in range(key):
            if not k.next:
                raise KeyError("List doesn't have node by key %s" % key)
            k = k.next

        return k

    def __setitem__(self, key, value):
        if not isinstance(value, Node):
            raise TypeError("Value should be an instance of Node class")

        node_to_replace = self.__getitem__(key)

        prev_node = None
        curr_node = self.head
        while curr_node and curr_node != node_to_replace:
            prev_node = curr_node
            curr_node = curr_node.next

        if not prev_node:
            # setting value to the head
            value.next = self.head.next
            self.head = value
            return

        prev_node.next = value
        value.next = curr_node.next

    def __delitem__(self, key):
        node_to_remove = self.__getitem__(key)
        if not node_to_remove:
            return False

        prev_node = None
        curr_node = self.head
        while curr_node and curr_node != node_to_remove:
            prev_node = curr_node
            curr_node = curr_node.next

        if not prev_node:
            self.head = curr_node.next
            return

        prev_node.next = curr_node.next

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
        l.add_last(node)
    print(l)

    print(l[5])

    l[5] = Node(42)
    print(l)

    del l[5]
    print(l)

