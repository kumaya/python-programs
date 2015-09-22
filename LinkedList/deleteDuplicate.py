# Delete duplicate items from a sorted linked list
# Input1: 1 -> 1 -> 2 -> 4 -> 4 -> 5-> 10 -> X
# Output1: 1 -> 2 -> 4 -> 5 -> 10 -> X

from linkedList import LinkedList


class RemoveDuplicatesFromSorted(object):
    def __init__(self, head=None):
        self.head = head

    def traverse_and_delete(self):
        """ Traverse the linked list and insert unique elements in new list
        :return: new linked list containing unique elements
        """
        current = self.head
        next_next = None
        new_list = LinkedList()
        if not current:
            return
        while current.get_next():
            if current.get_data() == current.get_next().get_data():
                new_list.insert_at_end(current.get_data())
                next_next = current.get_next().get_next()
                current = next_next
            else:
                new_list.insert_at_end(current.get_data())
                current = current.get_next()
        new_list.insert_at_end(current.get_data())
        return new_list


class Remove(object):
    def __init__(self, head=None):
        self.head = head

    def delete(self):
        current = self.head
        while current.get_next():
            if current.get_data() == current.get_next().get_data():
                current = current.get_next().get_next()
            else:
                current = current.get_next()


if __name__ == "__main__":
    llObj = LinkedList()
    llObj.insert(1)
    llObj.insert_at_end(1)
    llObj.insert_at_end(2)
    llObj.insert_at_end(4)
    llObj.insert_at_end(4)
    llObj.insert_at_end(5)
    llObj.insert_at_end(10)
    print "Original",
    llObj.printLinkedList(llObj.head)

    dLL = RemoveDuplicatesFromSorted(llObj.head)
    newLL = dLL.traverse_and_delete()
    print "Unique element",
    llObj.printLinkedList(newLL.head)