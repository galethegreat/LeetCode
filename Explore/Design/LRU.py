class Node:
    def __init__(self, key, val, next=None, prev=None):

        self.key = key
        self.val = val

        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _findLRU(self) -> Node:

        return self.head.next


    def add(self, node: Node) -> None:

        new_node = node
        prev = self.tail.prev

        self.tail.prev = new_node
        prev.next = new_node

        new_node.next = self.tail
        new_node.prev = prev

    def remove(self, node: Node)-> None:

        next, prev = node.next, node.prev
        prev.next, next.prev = next, prev

    def update(self, node: Node):
        self.remove(node)
        self.add(node)

    def popLRU(self) -> Node:

        lru = self._findLRU()

        self.remove(lru)

        return lru

class LRUCache:

    def __init__(self, capacity: int):

        self.size = 0
        self.capacity = capacity

        self.cache = dict()

        self.LRU = DoublyLinkedList()


    def get(self, key: int) -> int:

        if key in self.cache:

            self.LRU.update(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.cache:

            node = Node(key, value)

            self.cache[key] = node
            self.LRU.add(node)
            self.size += 1

            if len(self.cache) > self.capacity:

                lru = self.LRU.popLRU()
                del(self.cache[lru.key])
                self.size -= 1

        else:
            self.cache[key].val = value
            self.LRU.update(self.cache[key])
