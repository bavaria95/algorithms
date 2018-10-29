import linked_list

def reverse_list(l):
    prev_node = None
    curr_node = l.head
    next_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    l.head = prev_node

    return l.head


if __name__ == '__main__':
    import json
    l = linked_list.List()

    for i in range(20):
        node = linked_list.Node(i)
        l.add_last(node)

    reverse_list(l)
    assert json.loads(str(l)) == list(range(20))[::-1]


    l = linked_list.List()

    for i in range(2):
        node = linked_list.Node(i)
        l.add_last(node)

    reverse_list(l)
    assert json.loads(str(l)) == list(range(2))[::-1]
