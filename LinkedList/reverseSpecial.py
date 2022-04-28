class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head, left, right):
    dummy = Node(None)
    dummy.next = head
    startNodeForReversal = head
    preNodeStart = None
    count = 1
    while count < left:
        preNodeStart = startNodeForReversal
        startNodeForReversal = startNodeForReversal.next
        count += 1
    prevNode, nextNode = None, None
    current = startNodeForReversal
    while count <= right:
        nextNode = current.next
        current.next = prevNode
        prevNode = current
        current = nextNode
        count += 1
    if preNodeStart:
        preNodeStart.next = prevNode
    else:
        dummy.next = prevNode
    if startNodeForReversal:
        startNodeForReversal.next = nextNode
    return dummy.next


if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    left = 1
    right = 3
    p = reverse(head, left, right)
    while p:
        print p.val,
        p = p.next