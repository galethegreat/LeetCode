class MyCircularQueue:

    def __init__(self, k):
        self.queue = [-1]*k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):

        if not self.isFull():

            if self.head == -1:
                self.head += 1

            self.tail += 1

            if self.tail >= len(self.queue):
                self.tail = 0

            self.queue[self.tail] = value
            return True

        else:
            return False

    def deQueue(self):

        if not self.isEmpty():
            self.queue[self.head] = -1
            if self.head == self.tail:
                self.head = -2
                self.tail = -1

            self.head += 1
            if self.head >= len(self.queue):
                self.head = 0

            return True

        else:
            return False

    def Front(self):
        if not self.isEmpty():
            front = self.queue[self.head]
            return front
        else: return -1

    def Rear(self):
        if not self.isEmpty():
            rear = self.queue[self.tail]
            return rear
        else: return -1

    def isEmpty(self):
        if self.head == -1:
            return True

    def isFull(self):

        if self.tail >= self.head and self.tail - self.head == len(self.queue)- 1 and len(self.queue) != 1:

            return True

        elif self.head >= self.tail and self.head - 1 == self.tail:
            return True

        elif len(self.queue) == 1 and self.queue[0] != -1:
            return True

        elif len(self.queue) == 1 and self.queue[0] == -1:
            return False

        else:
            return False
