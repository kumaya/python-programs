# Program to reverse a linked list
from linkedList import LinkedList

def reverseLinkedList(head):
    prev = nextP = None
    current = head
    while current:
        nextP = current.get_next()
        current.set_next(prev)
        prev = current
        current = nextP
    return prev

def pairWiseSwap(head):
    if not head or not head.get_next():
        return
    prev = head
    curr = head.get_next()

    head.set_next(curr)

    while True:
        nextP = curr.get_next()
        curr.set_next(prev)
        if (nextP == None) or (nextP.get_next() is None):
            prev.set_next(nextP)
            break
        prev.set_next(nextP.get_next())
        prev = nextP
        curr = prev.get_next()
    return curr

def pairwise_ll_reversal(head):
    temp = temp1 = None
    current = head
    while current and current.get_next():
        temp = current.get_next()
        temp1 = temp.get_next()
        temp.set_next(current)
        current.set_next(temp1)
    return temp


if __name__ == "__main__":
    ll_obj = LinkedList()
    ll_obj.insert(1)
    ll_obj.insert(2)
    ll_obj.insert(3)
    ll_obj.insert(4)
    ll_obj.insert(5)
    ll_obj.insert(6)
    ll_obj.insert_at_end(54)
    ll_obj.printLinkedList(ll_obj.head)
    # head1 = reverseLinkedList(ll_obj.head)
    # print "Reversed", ll_obj.printLinkedList(head1)
    head2 = pairwise_ll_reversal(ll_obj.head)
    ll_obj.printLinkedList(head2)