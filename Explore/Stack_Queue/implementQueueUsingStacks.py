class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
        self.current_pop = 1


    def push(self, x):
        self.stack1.append(x)


    def pop(self):
        if self.current_pop == 1 and not self.empty():
            while len(self.stack1) > 0:

                self.stack2.append(self.stack1.pop())

            temp = self.stack2.pop()
            if len(self.stack2) > 0: self.current_pop = 2
            return temp

        elif self.current_pop == 2 and not self.empty():
            temp = self.stack2.pop()
            if len(self.stack2) == 0 :
                self.current_pop = 1
            return temp

        return None
    def peek(self):
        if not self.empty():
            if self.current_pop == 1:
                return self.stack1[0]
            else:
                return self.stack2[-1]

        return None

    def empty(self):
        if len(self.stack2) > 0 or len(self.stack1) > 0:
            return False
        else:
            return True

m = MyQueue()
m.push(1)
m.push(2)
print(m.peek())
print(m.pop())
print(m.current_pop)
print(m.peek())
print(m.empty())
print(m.pop())
m.push(4)
m.push(3)
print(m.pop())
m.push(5)
print(m.peek())
print(m.pop())
