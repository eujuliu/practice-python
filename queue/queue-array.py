class Queue:
    def __init__(self) -> None:
        self.values = []

    def __repr__(self) -> str:
        return " -> ".join(map(lambda value: str(value), self.values))

    def enqueue(self, value: any) -> None:
        self.values.append(value)

    def dequeue(self):
        return self.values.pop(0)

    def empty(self):
        self.values = []

        return self


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue("4")
queue.dequeue()
queue.enqueue({"id": 1231312, "value": "Hello"})

print(queue)
