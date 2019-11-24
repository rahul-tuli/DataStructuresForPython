class Node:
    __slots__ = "val", "next"

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return "Node({})".format(self.val)

    def __eq__(self, other):
        assert self and other, "Can't compare with None"
        return self.val == other.val and self.next == other.next


class LinkedList:
    __slots__ = "head", "current", "size"

    def __init__(self, another_list=[]):

        self.head = None
        self.current = None
        self.size = 0

        for item in another_list:
            self.append(item)

    def __str__(self):
        result = [str(node) for node in self]
        return "[" + ", ".join(result) + "]"

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        next_node = self.current

        if next_node is None:
            raise StopIteration

        self.current = self.current.next
        return next_node

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        """
        A function that returns the Node object at a particular index in the linked list
        supports negative indexing

        :precondition: index must be an integer between [-len(linked_list), len(linked_list) )
        :param item: index of the item to get
        :return: The Node at index = item
        """
        if item < 0:
            item = self.size + item

        for index, node in enumerate(self):
            if index == item:
                return node
        raise KeyError

    def __setitem__(self, key, value):
        self[key].val = value

    def __eq__(self, other):
        return self.head == other.head

    def append(self, value):
        """
        A function to append a value to the end of the linked list
        uses __getitem__()

        :param value: Value to be appended
        :return None
        """
        if self.head is None:
            self.head = Node(value)

        else:
            self[-1].next = Node(value)
        self.size += 1

    def pop(self):
        """
        A function that pops the last element off the linked list

        :return: The value at last element of the linked list
        """
        if self.head is None:
            # print("Nothing to pop, Take None")
            return None

        if self.head.next is None:
            to_pop = self.head.val
            self.head = None
            self.size -= 1
            return to_pop

        to_pop = self[-1].val
        self[-2].next = None
        self.size -= 1

        return to_pop

    def remove(self, value):
        """
        A function that removes the first occurence of avalue in the linked list

        :param value: The value to be removed
        :return: The removed value, or False
        """
        prev = None
        for node in self:
            if node.val == value:
                if prev:
                    prev.next = node.next
                    self.size -= 1
                    return node.val

                self.head = self.head.next
                self.size -= 1
                return node.val
            prev = node
        return False

    def insert(self, index, value):
        """
        A function to insert a value at a particular index in the linked list

        :param index: The index at which value is to be inserted
        :param value: The value to be inserted at specified index
        :pre: index should be an integer and with [0, len(linked_list)]
        """
        assert isinstance(index, int)
        if index > self.size or index < 0:
            raise IndexError

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        elif index == self.size:
            self[index - 1].next = new_node
        else:
            prev = self[index - 1]
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def get_list(self):
        return [node.val for node in self]


def test():
    print("Creation via List")
    linked_list = LinkedList(range(10))
    print(linked_list)

    print("Appending -9999")
    print("Before {}".format(linked_list))
    linked_list.append(-9999)
    print("After {}".format(linked_list))


import unittest


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.normal_list = list(range(10))
        self.linked_list = LinkedList(range(10))

    def _test_normal_list_and_linked_list(self):
        self.assertEqual(self.normal_list, self.linked_list.get_list())

    def test_get_list(self):
        self.assertEqual(self.linked_list.get_list(), [node.val for node in self.linked_list])

    def test_append(self):
        self.normal_list.append(5)
        self.linked_list.append(5)
        self._test_normal_list_and_linked_list()

    def test_insert(self):
        self.normal_list.insert(3, -9999)
        self.linked_list.insert(3, -9999)
        self._test_normal_list_and_linked_list()

    def test_pop(self):
        self.normal_list.pop()
        self.linked_list.pop()
        self._test_normal_list_and_linked_list()

    def test_pop_empty(self):
        new_ll = LinkedList()
        try:
            new_ll.pop()
            self.assertEqual([], new_ll.get_list())
        except:
            print("An error was thrown due to underflow")

    def test_remove(self):
        self.normal_list.remove(self.normal_list[0])
        self.linked_list.remove(self.linked_list[0].val)
        self._test_normal_list_and_linked_list()


if __name__ == '__main__':
    unittest.main(verbosity=2)
