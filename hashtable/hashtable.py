class Node:
    key: int
    value: any
    next: any

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.key}:{self.value}"


class LinkedList:
    head: Node | None
    tail: Node | None

    def __init__(self, key=None, value=None):
        self.head = None
        self.tail = None

        if key and value:
            self.add(key, value)

    def __str__(self) -> str:
        values = []
        n = self.head

        while n is not None:
            values.append(str(n))
            n = n.next

        return " -> ".join(values)

    def add(self, key, value):
        n = Node(key, value)

        if self.head is None:
            self.head = n
            self.tail = self.head
        else:
            self.tail.next = n
            self.tail = n

    def remove(self, key):
        prev = None
        node = self.head

        while True:
            prev = node
            node = node.next

            if node == None:
                return f"{key} don't exists"

            if node.key == key:
                prev.next = node.next

                if node.next == None:
                    self.tail = prev

                return f"key {key} removed"

    def exists(self, key):
        node = self.head
        
        while node:
            if node.key == key:
                return node

            node = node.next
            
        return node


class HashTable:
    capacity = int
    raw = list[LinkedList]

    def __init__(self, capacity):
        self.capacity = capacity
        self.raw = [LinkedList()] * capacity

    def hash(self, key: int):
        return key % self.capacity

    def add(self, key, value):
        code = self.hash(key)
        linked_list = self.raw[code]
        old = linked_list.exists(key)

        if linked_list and old:
            old_value = old.value
            old.value = value

            return f"({key}:{old_value}) updated to {value}"
        elif not old:
            linked_list.add(key, value)

            return f"({key}:{value}) added"
        else:
            


hash_table = HashTable(10)
print(hash_table.add(123, "124"))
