# Given a doubly linked list.
# Convert it to BST without using any extra space.


class Node(object):
    def __init__(self, key):
        self.__key = key
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__key

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, previous_pointer):
        self.__prev = previous_pointer

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_pointer):
        self.__next = next_pointer


def print_dll(head):
    temp = head
    while temp:
        print temp.data, "<==>",
        temp = temp.next_node
    print "X"


def count_nodes(head):
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next_node
    return count


def sorted_dll_to_bst_recur(head, n):
    # Base case
    if n <= 0:
        return
    left = sorted_dll_to_bst_recur(head.next_node, n//2)
    # head will be middle node after above recursion
    root = head
    # set dll prev as bst's left node
    root.prev = left
    # head = head.next_node
    root.next_node = sorted_dll_to_bst_recur(head.next_node, n - (n // 2) - 1)
    return root


def sorted_dll_to_bst(head):
    n = count_nodes(head)
    print "==>", head.data, n
    return sorted_dll_to_bst_recur(head, n)

if __name__ == "__main__":
    dll = Node(1)
    dll.next_node = Node(2)
    dll.next_node.next_node = Node(3)
    dll.next_node.next_node.next_node = Node(4)
    dll.next_node.next_node.next_node.next_node = Node(5)
    dll.next_node.next_node.next_node.next_node = Node(6)
    dll.next_node.next_node.next_node.next_node.next_node = Node(7)
    dll.next_node.prev = dll
    dll.next_node.next_node.prev = dll.next_node
    dll.next_node.next_node.next_node.prev = dll.next_node.next_node
    dll.next_node.next_node.next_node.next_node.prev = dll.next_node.next_node.next_node
    dll.next_node.next_node.next_node.next_node.next_node.prev = dll.next_node.next_node.next_node.next_node

    # print doubly linked list
    print_dll(dll)
    r = sorted_dll_to_bst(dll)
    print r.data
