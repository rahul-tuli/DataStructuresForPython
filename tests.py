import unittest
from LinkedList import LinkedList


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

    def test_reversal(self):
        self.assertEqual(list(reversed(self.normal_list)), [node.val for node in reversed(self.linked_list)])


if __name__ == '__main__':
    unittest.main(verbosity=2)
