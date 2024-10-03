import copy


class LinkedList:
    def __init__(self, value=None, nxt=None) -> None:
        self.value = value
        self.next = nxt

    def __iter__(self):
        item = self
        while item is not None:
            yield item
            item = item.next

    def __str__(self) -> str:
        values = []
        for node in self:
            if node:
                values.append(str(node.value))

        return " -> ".join(values)

    def size(self) -> int:
        values = []
        for node in self:
            values.append(node.value)

        return len(values)

    def empty(self):
        for node in self:
            if node is None:
                return True
        return False

    def value_at(self, index):
        values = []
        for node in self:
            values.append(node.value)

        return values[index]

    def push_front(self, value):
        nxt = LinkedList(self.value, self.next)
        self.value = value
        self.next = nxt

        return self

    def pop_front(self):
        value = self.value
        nxt = self.next

        if nxt:
            self.value = nxt.value
            self.next = nxt.next
        else:
            self.value = None

        return value

    def push_back(self, value):
        crrNode = None

        for node in self:
            if not node.next:
                crrNode = node

        crrNode.next = LinkedList(value)

        return self

    def pop_back(self):
        prev, nxt = None, None

        for node in self:
            prev = nxt
            nxt = node
            if node.next is None:
                prev.next = None

        return nxt.value

    def front(self):
        return self.value or None

    def back(self):
        last = None

        for node in self:
            if node.next is None:
                last = node.value

        return last

    def insert(self, index, value):
        crr_index = -1
        prev, nxt = None, self

        for node in self:
            crr_index += 1
            prev = nxt
            nxt = node

            if crr_index == index:
                new_link = LinkedList(value, nxt)
                prev.next = new_link

                return self

    def erase(self, index):
        crr_index = -1
        prev, nxt = None, self

        for node in self:
            crr_index += 1
            prev = nxt
            nxt = node

            if crr_index == index:
                prev.next = nxt.next

                return self

    def reverse(self):
        prev = None
        node = copy.deepcopy(self)

        while node is not None:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        return prev

    def value_n_from_end(self, n):
        return self.reverse().value_at(n)

    def remove_value(self, value):
        prev = None
        node = self

        while node is not None:
            if node.value == value:
                prev.next = node.next

                return node.value

            prev = node
            node = node.next


node = LinkedList(5, LinkedList(6, LinkedList(7, LinkedList(8))))

print(node.size())
print(node.empty())
print(node.value_at(2))
print(node.push_front(4))
print(node.pop_front())
print(node.push_back(9))
print(node.push_back(10))
print(node.push_back(11))
print(node.pop_back())
print(node.front())
print(node.back())
print(node.insert(2, 6.5))
print(node.erase(2))
print(node.value_n_from_end(2))
print(node.reverse())
print(node.remove_value(7))
print(node)
