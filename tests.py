import unittest
from LinkedList import *


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
        start, mid, end = 0, len(self.normal_list) // 2, -1
        for i in start, mid, end:
            self.normal_list.pop(i)
            self.linked_list.pop(i)
            self._test_normal_list_and_linked_list()

    def test_pop_empty(self):
        new_ll = LinkedList()
        try:
            new_ll.pop()
        except UnderFlow:
            pass

    def test_remove(self):
        start, mid, end = 0, len(self.normal_list) // 2, -1
        for i in start, mid, end:
            self.normal_list.remove(self.normal_list[i])
            self.linked_list.remove(self.linked_list[i].val)
            self._test_normal_list_and_linked_list()

    def test_remove_element_not_present(self):
        new_ll = LinkedList([5, 10])
        try:
            new_ll.remove(15)
        except ElementNotFoundError:
            pass

    def test_reversal(self):
        self.assertEqual(list(reversed(self.normal_list)), [node.val for node in reversed(self.linked_list)])

    def test_index_of(self):
        self.assertEqual(self.normal_list.index(self.normal_list[0]),
                         self.linked_list.index_of(self.linked_list.get(0)))

    def test_size(self):
        self.assertEqual(sum([1 for _ in self.linked_list]), len(self.linked_list))


if __name__ == '__main__':
    unittest.main(verbosity=3)
