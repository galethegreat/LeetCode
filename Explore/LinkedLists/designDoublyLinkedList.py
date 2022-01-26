class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0) #sentinel head
        self.tail = ListNode(0) #sentinel tail

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def get(self, index):
        if index >= self.size or index < 0: #TODO: check if it is index >= self.size
            return -1
        node = self.head
        for _ in range(index + 1 ):
            node = node.next
        return node.val

    def addAtHead(self, val):
        next_node = self.head.next
        previous_node = self.head

        new_node = ListNode(val)
        new_node.prev = previous_node
        new_node.next = next_node
        self.head.next = new_node
        next_node.prev = new_node
        self.size += 1

    def addAtTail(self, val):
        succ, pred = self.tail, self.tail.prev

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add


    def addAtIndex(self, index, val):
        if index > self.size:return None
        if index < 0: index = 0

        previous_node = self.head
        for _ in range(index):
            previous_node = previous_node.next

        next_node = previous_node.next

        new_node = ListNode(val)
        new_node.prev = previous_node
        new_node.next = next_node
        previous_node.next = new_node
        next_node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index >= self.size or index < 0: return None

        node = self.head.next
        for _ in range(index):
            node = node.next

        next_node = node.next
        previous_node = node.prev
        next_node.prev = previous_node
        previous_node.next = next_node
        self.size -= 1

def main():
    obj = MyLinkedList()
    obj.addAtHead(1)

    obj.addAtTail(3)
#obj.addAtTail(3)
    print(obj.get(0))
    print(obj.get(1))
    print("")
    obj.addAtIndex(1, 2)
    print(obj.get(0))
    print(obj.get(1))
    print(obj.get(2))
    obj.deleteAtIndex(3)
    print("")
    print(obj.get(0))
    print(obj.get(1))
    print(obj.get(2))
    obj.deleteAtIndex(1)
    print("")
    print(obj.get(0))
    print(obj.get(1))
    print(obj.get(2))

    #print(Solution().isPalindrome(head))

if __name__ == "__main__":
    main()
