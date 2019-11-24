class Node:
    __slots__ = "val", "next"

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val) + ","

    def __repr__(self):
        return "Node({})".format(self.val)

    # def __eq__(self, other):
    #     # print("checking Node {}".format(self))
    #     return self.val == other.val and self.next == other.next

    # def __eq__(self, other):
    #     assert self and other, "Comparision between a None objects is not possible"
    #     return self.val == other.val


class LinkedList(object):
    __slots__ = "head", "current", "size"

    def __init__(self):
        self.head = None
        self.current = None
        self.size = 0

    def __str__(self):
        result = []
        for node in self:
            result.append(str(node))
        return " ".join(result)

    def __iter__(self):
        # print("Iter was called")
        self.current = self.head
        return self

    def __next__(self):
        # print("next was called")

        next_node = self.current
        if next_node is None:
            raise StopIteration

        self.current = self.current.next
        return next_node

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        print("getitem was called")
        for index, node in enumerate(self):
            if index == item:
                return node

    def __setitem__(self, key, value):
        print("setitem was called")
        assert 0 <= key < len(self), "Wrong index"
        self[key].val = value


    def __eq__(self, other):
        return self.head == other.head

    def add(self, value):
        """
        Add a value to the Linked List
        :param value:
        :return:
        """
        if self.head is None:
            self.head = Node(value)

        else:
            for runner in self:
                continue
            runner.next = Node(value)
        self.size += 1

    def remove(self, value):
        prev = None

        for node in self:
            if node.val == value:
                if prev:
                    prev.next = node.next
                    self.size -= 1
                    return node

                self.head = self.head.next
                self.size -= 1
                return node
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


def test():
    my_list = LinkedList()
    my_list.add(5)
    my_list.add(10)
    my_list.add(15)
    my_list.add(20)
    my_list.add(25)
    my_list.add(30)



    print(my_list)

    my_list[3] = 999999999999999999

    print(my_list)

    #
    # print("for loop output")
    #
    # for element in my_list:
    #     print(element, end="\t")
    #
    # for i, element in enumerate(my_list):
    #     print(i, ")", element, end="\t")
    # my_list.remove(20)
    # print(my_list)
    #
    # my_list.remove(5)
    # print(my_list)
    #
    # my_list.insert(5, 2)
    # print(my_list)
    #
    # print(len(my_list))
    #
    # print(my_list[len(my_list) - 1])
    #
    # [print(node, end=" ") for node in reversed(my_list)]
    #
    # print(my_list == my_list)


if __name__ == '__main__':
    test()
