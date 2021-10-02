from node import Node


class Tree:
    tree = None

    def insert(self, value):
        node = Node(value)

        if not self.tree:
            self.tree = node
            return self

        current = self.tree

        while current.next:
            current = current.next

        current.next = node
        return self

    def to_list(self):
        list_ = []
        current = self.tree

        while current:
            list_.append(current.value)
            current = current.next

        return list_

    def reverse(self):
        prev = None
        current = self.tree

        while current:
            next_, current.next = current.next, prev
            prev, current = current, next_

        self.tree = prev
        return self
