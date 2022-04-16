from collections import defaultdict
class Node:
    '''doubly linked list node'''
    def __init__(self, key, value, freq=1, next=None, prev=None):

        self.key = key
        self.freq = freq

        self.val = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    '''doubly linked list with LRU tracking and updates'''

    def __init__(self):

        self._size = 0

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):

        return self._size

    def _getLRU(self) -> Node:

        return self.head.next

    def popLRU(self) -> Node:
        '''pops lru element from list and returns it'''

        lru = self._getLRU()
        self.remove_node(lru)

        return lru


    def add_node(self, node: Node):
        '''adds node to doubly linked list'''

        prev_tail = self.tail.prev

        self.tail.prev = node
        prev_tail.next = node

        node.next = self.tail
        node.prev = prev_tail

        self._size += 1


    def remove_node(self, node: Node):
        '''removes node from doubly linked list'''

        next_node, prev_node = node.next, node.prev
        prev_node.next, next_node.prev = next_node, prev_node

        self._size -= 1


    def update(self, node:Node):
        '''Updates node to MRU'''

        self.remove_node(node)
        self.add_node(node)


class LFUCache:

    def __init__(self, capacity: int):
        assert 0 <= capacity, f"Invalid capacity input {capacity}, must be greater or equal than 0 and"

        self.capacity = capacity

        self._size = 0
        self._min_freq = 0

        self.cache = dict()
        self.freq = defaultdict(DoublyLinkedList)


    def get(self, key: int) -> int:


        if key in self.cache:

            node = self._update(key)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:

        if self.capacity <= 0:
            return None

        if key not in self.cache:

            if len(self.cache) >= self.capacity:

                lru = self.freq[self._min_freq].popLRU()
                del(self.cache[lru.key])
                self._size -= 1

            node = Node(key, value)
            self._min_freq = 1

            self.cache[key] = node
            self.freq[self._min_freq].add_node(node)

            self._size += 1

        else:
            self.cache[key].val = value
            node = self._update(key)

    def _update(self, key: int)-> Node:

        node = self.cache[key]

        self.freq[node.freq].remove_node(node)

        if len(self.freq[node.freq]) == 0 and self._min_freq == node.freq:
            self._min_freq += 1

        node.freq += 1

        self.freq[node.freq].add_node(node)

        return node
