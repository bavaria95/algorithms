import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from hashmap.hashmap import Hash


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

    def __repr__(self):
        return "({}: {})".format(self.key, self.value)


class DoubleLinkedList(object):
    def __init__(self):
        self.num_elements = 0

        self.dummy_head = Node(None, None)
        self.dummy_tail = Node(None, None)

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def add(self, new_node):
        '''Add new element to the head of the list'''
        new_node.next = self.dummy_head.next
        new_node.prev = self.dummy_head
        self.dummy_head.next.prev = new_node
        self.dummy_head.next = new_node

        self.num_elements += 1

    def remove(self):
        '''Removes last element from the list'''
        rem = self.dummy_tail.prev
        rem.prev.next = self.dummy_tail
        self.dummy_tail.prev = rem.prev
        key = rem.key
        self.num_elements -= 1
        del rem

        return key

    def update_access(self, node):
        '''Moves node to the head'''
        node.prev.next = node.next
        node.next.prev = node.prev

        self.num_elements -= 1

        self.add(node)


class CacheLRU(object):
    def __init__(self, maxsize=50):
        self.maxsize = maxsize
        self.hash = Hash()
        self.list = DoubleLinkedList()

    def set(self, key, value):
        node = Node(key, value)

        self.hash[key] = node

        # if reached maximum capacity of our queue
        if self.list.num_elements >= self.maxsize:
            # remove last node in the list
            rem_key = self.list.remove()
            # remove this key from the hash
            del self.hash[rem_key]

        self.list.add(node)

    def get(self, key):
        node = self.hash.get(key, None)
        if not node:
            return None

        # pop node up to the list head
        self.list.update_access(node)

        return node


if __name__ == "__main__":
    cache = CacheLRU(5)

    for i in range(10):
        cache.set(i, i)

    for i in range(5):
        assert cache.get(i) is None

    for i in range(5, 10):
        assert i == cache.get(i).value
