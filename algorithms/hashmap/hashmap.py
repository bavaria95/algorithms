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
        self.buckets = Hash.__allocate_buckets(buckets_size)
        self.num_keys = 0

    @staticmethod
    def __allocate_buckets(buckets_size):
        return [List() for _ in range(buckets_size)]

    @property
    def load_factor(self):
        return float(self.num_keys) / self.buckets_size

    def resize_up(self):
        # create a new hash with double buckets size
        new_hash = Hash(self.buckets_size * 2)

        # copy elements to the new hash
        for key, value in self.items():
            new_hash[key] = value

        # trick to replace current object with a new one
        self.__dict__.update(new_hash.__dict__)

    def resize_down(self):
        new_hash = Hash(int(self.buckets_size * 0.5))

        for key, value in self.items():
            new_hash[key] = value

        # trick to replace current object with a new one
        self.__dict__.update(new_hash.__dict__)

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
        if self.load_factor > 0.75:
            self.resize_up()

        index = self.__get_bucket_index(key)
        node = self.__get(key)
        llist = self.buckets[index]

        if node:
            llist.remove_node(node)
            self.num_keys -= 1

        new_node = HashNode(key, value)
        llist.add_last(new_node)
        self.num_keys += 1


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

    def get(self, key, *default):
        if len(default) > 1:
            raise TypeError('get() expected 2 arguments, got {} instead'.format(len(default) + 1))

        node = self.__get(key)
        if node:
            return node.value

        if len(default):
            return default[0]

        self.__missing__(key)

    def __delitem__(self, key):
        if self.buckets_size > 1024 and self.load_factor < 0.1:
            self.resize_down()

        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        node = self.__find_node_by_key(llist, key)

        if not node:
            raise KeyError('Key {} is missing in dictionary'.format(key))

        llist.remove_node(node)
        self.num_keys -= 1

    def __missing__(self, key):
        raise KeyError('Key {} is missing in dictionary'.format(key))

    def __len__(self):
        return self.num_keys

    def __contains__(self, key):
        return self.__get(key)

    def __iter__(self):
        self.iter_bucket_index = 0
        self.iter_prev = None

        return self

    def __next__(self):
        if self.iter_prev and self.iter_prev.next:
            self.iter_prev = self.iter_prev.next
            return self.iter_prev.key

        if not self.iter_prev and self.buckets[self.iter_bucket_index].head:
            self.iter_prev = self.buckets[self.iter_bucket_index].head
            return self.buckets[self.iter_bucket_index].head.key

        self.iter_bucket_index += 1
        while self.iter_bucket_index < self.buckets_size and not self.buckets[self.iter_bucket_index].head:
            self.iter_bucket_index += 1
        if self.iter_bucket_index >= self.buckets_size:
            raise StopIteration

        if self.buckets[self.iter_bucket_index].head:
            self.iter_prev = self.buckets[self.iter_bucket_index].head
            return self.buckets[self.iter_bucket_index].head.key

        raise StopIteration

    def items(self):
        iter_bucket_index = 0
        iter_prev = None

        for iter_bucket_index in range(self.buckets_size):
            it = self.buckets[iter_bucket_index].head
            while it:
                yield (it.key, it.value)
                it = it.next

        raise StopIteration


if __name__ == '__main__':
    d = Hash(10)

    assert len(d) == 0
    assert 'key1' not in d

    d['key1'] = 'value1'
    d['key2'] = 'value2'
    d['key3'] = 'value3'

    assert len(d) == 3
    assert 'key1' in d
    assert d['key3'] == 'value3'
    assert d['key1'] == 'value1'

    # TODO
    # use proper testing tool
    try:
        d['key42']
        raise AssertionError('KeyError was supposed to be raised')
    except KeyError:
        pass
    assert 'key42' not in d

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

    assert d.get('key3', '') == 'new_value3'
    assert d.get('key42', '') == ''
    try:
        d.get('key42')
        raise AssertionError('KeyError was supposed to be raised')
    except KeyError:
        pass

    d['key4'] = 'value4'
    d['key5'] = 'value5'

    assert set([k for k in d]) == set(['key2', 'key3', 'key4', 'key5'])
