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

    def __setitem__(self, key, value):
        index = self.__get_bucket_index(key)
        node = self.__get(key)
        llist = self.buckets[index]

        if node:
            llist.remove_node(node)

        new_node = HashNode(key, value)

        llist.add_last(new_node)

    def __get(self, key):
        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        node = self.__find_node_by_key(llist, key)

        return node

    def __getitem__(self, key):
        node = self.__get(key)
        if node:
            return node.value

        self.__missing__(key)

    def __delitem__(self, key):
        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        node = self.__find_node_by_key(llist, key)

        if not node:
            raise KeyError('Key {} is missing in dictionary'.format(key))

        llist.remove_node(node)

    def __missing__(self, key):
        raise KeyError('Key {} is missing in dictionary'.format(key))

    def __len__(self):
        return sum([len(llist) for llist in self.buckets])

if __name__ == '__main__':
    d = Hash(10)

    assert len(d) == 0

    d['key1'] = 'value1'
    d['key2'] = 'value2'
    d['key3'] = 'value3'

    assert len(d) == 3

    assert d['key3'] == 'value3'
    assert d['key1'] == 'value1'

    # TODO
    # use proper testing tool
    try:
        d['key42']
        raise AssertionError('KeyError was supposed to be raised')
    except KeyError:
        pass

    del d['key1']
    try:
        d['key1']
        raise AssertionError('KeyError was supposed to be raised')
    except KeyError:
        pass

    assert len(d) == 2


    d['key3'] = 'new_value3'
    assert d['key3'] == 'new_value3'

    assert len(d) == 2
