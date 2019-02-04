import os, sys
import collections
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from list.linked_list import Node, List

class HashNode(Node):
    def __init__(self, key, value):
        super().__init__(value)
        self.key = key

    def __repr__(self):
        return '{} -> {}'.format(self.key, self.value)


class Hash(object):
    def __init__(self, buckets_size=1024):
        self.buckets_size = buckets_size
        self.buckets = [List() for _ in range(buckets_size)]

    @staticmethod
    def __check_if_key_hashable(key):
        if not isinstance(key, collections.Hashable):
            raise TypeError('Key {} is unhashable'.format(key))
        return True

    def __get_bucket_index(self, key):
        Hash.__check_if_key_hashable(key)
        index = hash(key) % self.buckets_size

        return index

    def __find_node_by_key(self, llist, key):
        for node in llist:
            if node.key == key:
                return node

        return None

    def set(self, key, value):
        index = self.__get_bucket_index(key)
        node = HashNode(key, value)

        self.buckets[index].add_last(node)

    def get(self, key):
        index = self.__get_bucket_index(key)

        llist = self.buckets[index]

        node = self.__find_node_by_key(llist, key)

        if node:
            return node.value
        return None

    def delete(self, key):
        index = self.__get_bucket_index(key)

        llist = self.buckets[index]

        node = self.__find_node_by_key(llist, key)

        if node:
            llist.remove_node(node)


if __name__ == '__main__':
    d = Hash(10)

    d.set('key1', 'value1')
    d.set('key2', 'value2')
    d.set('key3', 'value3')

    assert d.get('key3') == 'value3'
    assert d.get('key1') == 'value1'

    assert d.get('key42') is None

    d.delete('key1')
    assert d.get('key1') is None

    d.delete('key42')
    assert d.get('key42') is None
