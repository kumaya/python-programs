# Given a linked list with alternate sorted order in ascending and descending order respectively.
# Return the list in sorted order.
# Input: 10 -> 59 -> 48 -> 39 -> 69 -> 21 -> 98 -> 12 -> X
# Output: 10 -> 12 -> 21 -> 39 -> 48 -> 59 -> 69 -> 98 -> X


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return  self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    @staticmethod
    def print_linked_list(head):
        current = head
        while current:
            print current.get_data(),
            print "->",
            current = current.get_next()
        print "X"


class SortLinkedList(object):
    def __init__(self, head=None):
        self.llHead = head

    @staticmethod
    def reverse_linked_list(head):
        current = head
        prev = next_ptr = None
        while current:
            next_ptr = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_ptr
        return prev

    def get_linked_list(self):
        current = self.llHead

        # Create ascending ordered linked list
        new_ll1 = LinkedList()
        while current:
            new_ll1.insert(current.get_data())
            current = current.get_next()
            if current:
                current = current.get_next()
        new_ll = self.reverse_linked_list(new_ll1.head)

        # Create descending ordered linked list
        new_ll2 = LinkedList()
        current = self.llHead
        while current:
            current = current.get_next()
            if current:
                new_ll2.insert(current.get_data())
            current = current.get_next()

        return new_ll, new_ll2.head

    def merge_linked_list(self, head1, head2):
        new_ll = LinkedList()
        while head1 and head2:
            if head1.get_data() < head2.get_data():
                new_ll.insert(head1.get_data())
                head1 = head1.get_next()
            elif head1.get_data() > head2.get_data():
                new_ll.insert(head2.get_data())
                head2 = head2.get_next()
            else:
                new_ll.insert(head1.get_data())
                new_ll.insert(head2.get_data())
                head1 = head1.get_next()
                head2 = head2.get_next()
        while head1:
            new_ll.insert(head1.get_data())
            head1 = head1.get_next()
        while head2:
            new_ll.insert(head2.get_data())
            head2 = head2.get_next()
        temp = self.reverse_linked_list(new_ll.head)
        return temp

if __name__ == "__main__":
    llObj = LinkedList()
    llObj.insert(12)
    llObj.insert(98)
    llObj.insert(21)
    llObj.insert(69)
    llObj.insert(39)
    llObj.insert(48)
    llObj.insert(59)
    llObj.insert(10)

    print "Original Linked List: ",
    llObj.print_linked_list(llObj.head)

    sortedLLObj = SortLinkedList(llObj.head)
    val1, val2 = sortedLLObj.get_linked_list()
    print "Ascending ordered linked list: ",
    llObj.print_linked_list(val1)
    print "Descending ordered linked list: ",
    llObj.print_linked_list(val2)

    mergedLinkedList = sortedLLObj.merge_linked_list(val1, val2)

    print "Sorted Linked List: ",
    llObj.print_linked_list(mergedLinkedList)