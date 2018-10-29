import linked_list

# monkey patching to add this method of comparing nodes only here
def eq_node(self, key):
    return self.value == key
linked_list.Node.__eq__ = eq_node


def is_palindrom(l):
    # putting first half of the list to the stack
    first_half = []

    # using method of two pointers (one going through all elements
    # and another one by skipping every other)
    slow_node = l.head
    fast_node = l.head

    odd_length = False
    while fast_node:
        first_half.append(slow_node)
        slow_node = slow_node.next
        fast_node = fast_node.next
        if not fast_node:
            odd_length = True
            break
        fast_node = fast_node.next

    if odd_length:
        first_half.pop()

    while slow_node:
        stack_node = first_half.pop()
        if not stack_node == slow_node:
            return False
        slow_node = slow_node.next

    if first_half:
        return False

    return True


if __name__ == '__main__':
    def _run_test(data, correct):
        l = linked_list.List()

        for item in data:
            node = linked_list.Node(item)
            l.add_last(node)

        assert is_palindrom(l) == correct

    _run_test(['a'], True)
    _run_test(['a', 'a'], True)
    _run_test(['a', 'b'], False)
    _run_test(['a', 'b', 'a'], True)
    _run_test(['a', 'b', 'b'], False)
