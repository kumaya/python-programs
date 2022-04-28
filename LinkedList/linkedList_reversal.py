# Program to reverse and pairwise reverse a linked list
from linkedListProperty import LinkedList


def reverse_linked_list(head):
    prev = nextP = None
    current = head
    while current:
        nextP = current.node
        current.node = prev
        prev = current
        current = nextP
    return prev


def reverseLLRecursion(head):
    # return if empty
    if not head:
        return head
    # return if last node
    if not head.node:
        return head
    lastNode = reverseLLRecursion(head.node)
    head.node.node = head
    head.node = None
    return lastNode


def pairwise_reversal(head):
    current = head
    dummy = current.node
    while current and current.node:
        next = current.node
        next_to_next = next.node
        next.node = current
        if next_to_next and next_to_next.node:
            current.node = next_to_next.node
        else:
            current.node = next_to_next
        current = next_to_next
    return dummy


def create_linked_list():
    ll_obj = LinkedList()
    ll_obj.insert(1)
    ll_obj.insert(2)
    ll_obj.insert(3)
    ll_obj.insert(4)
    ll_obj.insert(5)
    ll_obj.insert(6)
    ll_obj.insert_at_end(54)
    return ll_obj.head


def printLinkedList(head):
    current = head
    print "Linked List: ",
    while current:
        print current.data,
        print "-->",
        current = current.node
    print "X"

if __name__ == "__main__":
    linked_list1 = create_linked_list()
    printLinkedList(linked_list1)
    new_head = reverse_linked_list(linked_list1)
    print "Reversed",
    printLinkedList(new_head)
    linked_list3 = create_linked_list()
    new_head = reverseLLRecursion(linked_list3)
    print "Reversed (recusrion)",
    printLinkedList(new_head)
    print "*" * 80
    linked_list2 = create_linked_list()
    printLinkedList(linked_list2)
    new_head = pairwise_reversal(linked_list2)
    print "Pairwise reversed",
    printLinkedList(new_head)