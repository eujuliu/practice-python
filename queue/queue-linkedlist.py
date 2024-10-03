class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value: any | None = value
        self.next: Node | None = next

    def __repr__(self) -> str:
        return str(self.value)


class Queue:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        values = []

        for node in self:
            values.append(str(node.value))

        return " -> ".join(values)

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dequeue(self):
        value = self.head.value

        self.head = self.head.next

        return value

    def empty(self):
        self.head = None

        return self.head


queue = Queue()

queue.enqueue({"value": 1})
queue.enqueue({"value": 2})
queue.enqueue({"value": 3})
queue.enqueue({"value": 4})

print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.empty())
