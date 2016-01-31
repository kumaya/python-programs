# Given linked list and two nodes in the list. Swap the nodes.
# Input: head, node1 and node2

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


def swap_nodes(head, x, y):
    some = head
    if x == y:
        return some

    if not head:
        return some

    prev = nodeX = nodeY = prevNodeX = prevNodeY = None
    foundNodeX = foundNodey = foundBothNodes = 0

    # Get nodeX, nodeY, previous of nodeX and nodeY respectively
    # These values will be required while swap
    while head and foundBothNodes == 0:
        if head.get_data == x:
            prevNodeX = prev
            nodeX = head
            foundNodeX = 1

        if head.get_data == y:
            prevNodeY = prev
            nodeY = head
            foundNodey = 1

        prev = head
        head = head.get_node

        if foundNodeX == 1 and foundNodey == 1:
            foundBothNodes = 1

    # If nodeX is head; make nodeY as head after swap
    if prevNodeX:
        prevNodeX.get_node = nodeY
    else:
        some = nodeY

    # If nodeY is head; make nodeX as head after swap
    if prevNodeY:
        prevNodeY.get_node = nodeX
    else:
        some = nodeX

    # While swapping links will get modified leading to loss of original
    #  link from X, so store it in a temp var.
    temp = nodeX.get_node
    nodeX.get_node = nodeY.get_node
    nodeY.get_node = temp

    return some

if __name__ == "__main__":
    ll = Node(1)
    ll.get_node = Node(2)
    ll.get_node.get_node = Node(3)
    ll.get_node.get_node.get_node = Node(4)
    ll.get_node.get_node.get_node.get_node = Node(5)

    print "Linked list: "
    print_list(ll)

    print "Swapped list: "
    head = swap_nodes(ll, 3, 1)
    print_list(head)