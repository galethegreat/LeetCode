class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:

        if 0 <= index < self.size:

            node = self.head

            for _ in range(index):
                node = node.next

            return node.next.val

        return -1

    def addAtHead(self, val: int) -> None:

        next_head = self.head.next

        self.head.next = Node(val, self.head.next, self.head)

        next_head.prev = self.head.next

        self.size += 1

    def addAtTail(self, val: int) -> None:
        prev_tail = self.tail.prev
        self.tail.prev = Node(val, self.tail, self.tail.prev)
        prev_tail.next = self.tail.prev
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        #assert 0 <= index <= self.size, f"Invalid Index {index}"

        if 0 <= index <= self.size:

            node = self.head

            for _ in range(index):
                node = node.next

            next_node = node.next

            node.next = Node(val, node.next, node)

            next_node.prev = node.next

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:

            node = self.head

            for _ in range(index):
                node = node.next

            next_next_node = node.next.next
            node.next = node.next.next
            next_next_node.prev = node

            self.size -= 1
