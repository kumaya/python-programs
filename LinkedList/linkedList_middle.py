# Program to find the middle element of a linked list

from linkedList import LinkedList


def middle_element(head):
    ptr1 = head
    ptr2 = head
    while ptr1:
        ptr1 = ptr1.get_next()
        if ptr1:
            ptr1 = ptr1.get_next()
            ptr2 = ptr2.get_next()
    return ptr2.get_data()


if __name__ == "__main__":
    ll_obj = LinkedList()
    ll_obj.insert(1)
    ll_obj.insert(2)
    ll_obj.insert(3)
    ll_obj.insert(4)
    ll_obj.insert(5)
    ll_obj.insert(6)
    ll_obj.insert_at_end(54)
    ll_obj.insert(123)
    ll_obj.printLinkedList(ll_obj.head)
    print "Middle element is: ", middle_element(ll_obj.head)
