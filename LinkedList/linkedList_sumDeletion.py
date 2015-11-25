# Program to delete the consecutive nodes it their sum is equal to given value
# e.g. Input1: 1 -> 2 -> 3 -> 4 -> X
# Input2: val=5
# Output: 1 -> 4 -> X
from linkedListProperty import LinkedList


def delete_pairs(head, val):
    if head is None or head.node is None:
        return head
    next_node = delete_pairs(head.node, val)
    if next_node and (head.data + next_node.data == val):
        head = next_node.node
    else:
        head.node = next_node
    return head


def create_linked_list(ll):
    ll.insert(6)
    ll.insert(1)
    ll.insert(6)
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert(5)
    ll.insert(2)
    ll.insert(5)
    ll.insert(2)
    # ll.insert(12)
    # ll.insert(10)
    # ll.insert(10)
    # ll.insert(19)
    # ll.insert(1)
    return ll.head


if __name__ == "__main__":
    ll = LinkedList()
    link_list = create_linked_list(ll)
    ll.printLinkedList(link_list)

    # Call to function
    value = 7
    final_head = delete_pairs(link_list, value)
    ll.printLinkedList(final_head)
