class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(-1)

    def get(self, index: int) -> int:

        if 0 <= index < self.size:

            node = self.head

            for _ in range(index):
                node = node.next

            return node.next.val

        return -1

    def addAtHead(self, val: int) -> None:

        self.head.next = Node(val, self.head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        #assert 0 <= index <= self.size, f"Invalid Index {index}"

        if 0 <= index <= self.size:

            node = self.head

            for _ in range(index):
                node = node.next

            node.next = Node(val, node.next)

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:

            node = self.head

            for _ in range(index):
                node = node.next

            node.next = node.next.next
