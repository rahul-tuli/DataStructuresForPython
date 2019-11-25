"""A class that emulates a Singly Linked List Node"""


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
        # assert self and other, "Can't compare with None"
        if self is None and other is None:
            return True
        if self is None or other is None:
            return False
        return self.val == other.val and self.next == other.next

    def __lt__(self, other):
        assert self and other
        return self.val < other.val
