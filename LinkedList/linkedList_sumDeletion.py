# Program to delete the consecutive nodes it their sum is equal to given value
# e.g. Input1: 1 -> 2 -> 3 -> 4 -> X
# Input2: val=5
# Output: 1 -> 4 -> X
from linkedListProperty import LinkedList


def delete_pairs(head, val):
    current = head
    next = current.node
    if (current.data + next.data) == val:
        some = next.node
    else:
        some = current

    if current.node:
        next = current.node
        if next:
            next2 = next.node
    while next2 and next:
        if next.data + next2.data == val:
            current.node = next2.node
            next = next2.node
            next2 = next2.node
        else:
            current = current.node
            next = next.node
            next2 = next2.node
    return some


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
    return ll.head


if __name__ == "__main__":
    ll = LinkedList()
    link_list = create_linked_list(ll)
    ll.printLinkedList(link_list)

    # Call to function
    value = 7
    final_head = delete_pairs(link_list, value)
    ll.printLinkedList(final_head)
