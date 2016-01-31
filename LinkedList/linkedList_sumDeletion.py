# Program to delete the consecutive nodes it their sum is equal to given value
# e.g. Input1: 1 -> 2 -> 3 -> 4 -> X
# Input2: val=5
# Output: 1 -> 4 -> X
from linkedListProperty import LinkedList


def delete_pairs(head, val):
    some = head
    prev = None
    while head:
        v1 = head
        v2 = head.node
        if v2 and v1.data + v2.data == val:
            if not prev:
                some = v2.node
            else:
                prev.node = v2.node
            head = v2.node
        else:
            prev = head
            head = head.node
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
