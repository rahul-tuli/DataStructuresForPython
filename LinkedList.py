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
        return "[" + ",".join(result) + "]"

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
        for index, node in enumerate(self):
            if index == item:
                return node.val
        raise KeyError

    def __setitem__(self, key, value):
        self[key].val = value

    def __eq__(self, other):
        return self.head == other.head

    def append(self, value):
        """
        A function to append a value to the end of the linked list
        :pre-condition: uses __getitem__():
        :param value: Value to be appended
        :return None
        """
        if self.head is None:
            self.head = Node(value)

        else:
            self[-1].next = Node(value)
        self.size += 1

    def pop(self):
        if self.head is None:
            print("Nothing to pop, Take None")
            return None

        if self.head.next is None:
            to_pop = self.head.val
            self.head = None
            self.size -= 1
            return to_pop

        to_pop = self[-1].val
        del self[-1]
        self[-2].next = None
        self.size -= 1

        return to_pop

    def remove(self, value):
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

    def insert(self, value, index):
        prev = None
        if index >= self.size or index < 0:
            raise IndexError

        for i, node in enumerate(self):
            if i == index:
                if prev:
                    next_element = prev.next
                    prev.next = Node(value)
                    prev.next.next = next_element
                    self.size += 1
                    return True

                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node
                self.size += 1
                return True

            prev = node
        return False

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



if __name__ == '__main__':
    test()
