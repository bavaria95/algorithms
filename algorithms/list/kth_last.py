import linked_list

def kth_last(l, k):
    gap_node = l.head

    # creating a gap of k items between two pointers
    for _ in range(k):
        if not gap_node:
            raise KeyError("There a less than k items in the list")
        gap_node = gap_node.next

    curr_node = l.head
    while gap_node:
        curr_node = curr_node.next
        gap_node = gap_node.next

    if not curr_node:
        raise KeyError("Not valid value of k")

    return curr_node

if __name__ == '__main__':
    l = linked_list.List()

    for i in range(20):
        node = linked_list.Node(i)
        l.add_last(node)

    kth_from_the_end_node = kth_last(l, 5)
    assert kth_from_the_end_node.value == 15

    kth_from_the_end_node = kth_last(l, 20)
    assert kth_from_the_end_node.value == 0
