# Given a singly linked list, m and n; where m = mth node
# delete next consecutive n nodes.


class Node():
    def __init__(self, data):
        self.__data = data
        self.__node = None

    @property
    def get_data(self):
        return self.__data

    @property
    def get_node(self):
        return self.__node

    @get_node.setter
    def get_node(self, node):
        self.__node = node


def print_list(head):
    while head:
        print head.get_data,
        head = head.get_node
    print ""


def modify_linked_list(head, m, n):
    some = head
    count = 1
    while head:
        if count == m:
            temp = head
            count1 = 0
            while head and count1 != n:
                head = head.get_node
                count1 += 1
            if head:
                temp.get_node = head.get_node
                head = head.get_node
            else:
                temp.get_node = head
            count = 0
        else:
            head = head.get_node
        count += 1
    return some


if __name__ == "__main__":
    ll = Node(1)
    ll.get_node = Node(2)
    ll.get_node.get_node = Node(3)
    ll.get_node.get_node.get_node = Node(4)
    ll.get_node.get_node.get_node.get_node = Node(5)
    ll.get_node.get_node.get_node.get_node.get_node = Node(6)
    ll.get_node.get_node.get_node.get_node.get_node.get_node = Node(7)

    print "Linked list: "
    print_list(ll)

    m = 1
    n = 2
    print "Modified linked list for m = %s and n = %s" % (m,n)
    new_lists_head = modify_linked_list(ll, m, n)
    print_list(new_lists_head)
