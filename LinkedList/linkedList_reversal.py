# Program to reverse a linked list
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


def pairwise_reversal(head):
    temp = temp1 = None
    current = head
    some = current.node
    while current and current.node:
        temp = current.node
        temp1 = temp.node
        temp.node = current
        if temp1 and temp1.node:
            current.node = temp1.node
        else:
            current.node = temp1
        current = temp1
    return some


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
    print "*"*80
    linked_list2 = create_linked_list()
    printLinkedList(linked_list2)
    new_head = pairwise_reversal(linked_list2)
    print "Pairwise reversed",
    printLinkedList(new_head)