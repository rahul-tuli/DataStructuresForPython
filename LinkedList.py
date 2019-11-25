"""A class that emulates a linked list"""
from SinglyLinkedListNode import Node
from LinkedListExceptions import *


class LinkedList:
    __slots__ = "head", "current", "size"

    def __init__(self, another_list=[]):
        self.head = self.current = None
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
        assert isinstance(item, int)
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

    def get(self, index):
        return self[index].val

    def set(self, index, value):
        self[index] = value

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

    def pop(self, index=None):
        """
        A function that pops the last element off the linked list

        :return: The value at last element of the linked list
        """
        if index is None:
            index = -1
        if len(self) == 0:
            raise UnderFlow

        return self._remove_at_index(index=index)

    def remove(self, value):
        """
        A function that removes the first occurence of avalue in the linked list

        :param value: The value to be removed
        :return: True if removed, else False
        """
        index = self.index_of(value)
        return self._remove_at_index(index)

    def _remove_at_index(self, index=False):
        if index is not False:
            if index == 0:
                to_remove = self.head
                self.head = self.head.next
            else:
                to_remove = self[index]
                self[index - 1].next = self[index].next

            self.size -= 1
            return to_remove
        raise ElementNotFoundError

    def index_of(self, value):
        """
        Returns the index of first occurence of value in the linked list if found else False

        :param value: The value to search for
        :return: The index of first occurence of value in the linked list if found else False
        """
        for i, node in enumerate(self):
            if node.val == value:
                return i
        return False

    def insert(self, index, value):
        """
        A function to insert a value at a particular index in the linked list

        :param index: The index at which value is to be inserted
        :param value: The value to be inserted at specified index
        :pre: index should be an integer and with [0, len(linked_list)]
        """
        assert isinstance(index, int)
        if index < 0:
            index = self.size + index

        if index > self.size or index < 0:
            raise IndexError

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            # self.size += 1
        elif index == self.size:
            print(index)
            self[index - 1].next = new_node
        else:
            prev = self[index - 1]
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def get_list(self):
        return [node.val for node in self]
