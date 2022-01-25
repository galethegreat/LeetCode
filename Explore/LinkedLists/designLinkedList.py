class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        if index >= self.size or index < 0 : return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val):
        self.addAtIndex(0,val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size: return None
        if index < 0: index = 0
        self.size += 1
        node_to_add = ListNode(val)
        previous_node = self.head
        for node in range(index):
            previous_node = previous_node.next
        temp_node = previous_node.next
        previous_node.next = node_to_add
        node_to_add.next = temp_node

    def deleteAtIndex(self, index):
        if index >= self.size or index < 0 : return None
        node = self.head
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1
