"""A class that emulates a linked list"""
from SinglyLinkedListNode import Node
from LinkedListExceptions import *

__author__ = "Rahul Tuli"
__email__ = "rt3991@rit.edu"
__status__ = "Under-Development"


class LinkedList(object):
    __slots__ = "head", "current", "size"

    def __init__(self, values=[]):
        """
        A method to initialize a linked list, user may or may not give a initial
        list of values

        :param values: Optional, An Iterable of values to initialize Linked List
                       with
        """
        self.head = self.current = None
        self.size = 0
        self.extend(values)

    def __str__(self):
        """
        A method that returns a string representation of the current Linked List
        :return: string representation of the Linked List
        """
        return "[" + ", ".join([str(node) for node in self]) + "]"

    def __len__(self):
        """
        A method that returns the current size of the LinkedList when len(..) is
         called
        :return: size of the Linked List
        """
        return self.size

    def __iter__(self):
        """
        A  method that returns an iterator for the Linked List
        :return: self, which is an iterator
        """
        self.current = self.head
        return self

    def __next__(self):
        """
        A method that returns the current state, and moves the pointer to the
        next element in the Linked List
        :return: current state
        """
        if self.current is None:
            raise StopIteration
        next_node = self.current
        self.current = self.current.next
        return next_node

    def __getitem__(self, item):
        """
        A function that returns the Node object at a particular index in the linked list
        supports negative indexing
        :precondition: index must be an integer between [-len(linked_list), len(linked_list) )
        :param item: index of the item to get
        :exception : raises KeyError if index not in Linked List
        :return: The Node at index = item
        """
        assert isinstance(item, int)
        if item < 0:
            item = self.size + item

        if item < 0 or item >= self.size:
            raise IndexError

        for index, node in enumerate(self):
            if index == item:
                return node

    def __setitem__(self, key, value):
        """
        A method that sets the value of node at index = key to the new value
        :param key: The index of Node in Linked List
        :param value: The new Value
        :return: None
        """
        self[key].val = value

    def __eq__(self, other):
        """
        A method to recursively check equality of two Linked Lists
        :param other: The second Linked List
        :return: True if equal else False
        """
        return self.head == other.head

    def __add__(self, other):
        """
        A method to connect two linked lists via '+' operator
        :param other: The second linked list
        :return:
        """
        assert other
        for current in self:
            continue
        current.next = other.head

    def get(self, index):
        """
        A method to get the value at a given Index
        :param index: The index whose value is to be returned
        :return: The value of Node at given index
        """
        return self[index].val

    def set(self, index, value):
        """
        A method to set the value at a given Index
        :param index: The index whose value is to be set
        :return: None
        """
        self[index] = value

    def extend(self, values):
        """
        A method to extend the linked list with values in the given iterable
        :param values: An iterable with values to be extended with
        :return: None
        """
        for value in values:
            self.append(value)

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

    def _remove_at_index(self, index=False):
        """
        A helper function internally used by pop, remove to remove element at a
        given index
        :param index: The index of element to be removed
        :exception : raises ElementNotFoundError if element not present at index
        :return: the removed element if successful else raises Exception
        """
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

    def remove(self, value):
        """
        A function that removes the first occurence of avalue in the linked list

        :param value: The value to be removed
        :return: True if removed, else False
        """
        index = self.index_of(value)
        return self._remove_at_index(index)

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
        elif index == self.size:
            print(index)
            self[index - 1].next = new_node
        else:
            prev = self[index - 1]
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def get_list(self):
        """
        A method that returns a list representation of the linked list
        :return: A list representation of the Linked List
        """
        return [node.val for node in self]
