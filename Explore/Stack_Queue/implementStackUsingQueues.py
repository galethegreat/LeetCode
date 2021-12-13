from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.current_pop = 1
    def push(self, x):
        if self.current_pop == 1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self):
        if self.current_pop == 1 and not self.empty():
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            temp = self.q1.popleft()
            self.current_pop = 2
            return temp
        elif self.current_pop == 2 and not self.empty():
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            temp = self.q2.popleft()
            self.current_pop = 1
            return temp
        else:
            return None
    def top(self):
        if self.current_pop == 1 and not self.empty():
            return self.q1[-1]
        elif self.current_pop == 2 and not self.empty():
            return self.q2[-1]
        else:
            return None
    def empty(self):
        if len(self.q1) > 0 or len(self.q2) > 0:
            return False
        else:
            return True

m = MyStack()
m.push(1)
m.push(2)
print(m.top())
print(m.pop())
m.push(3)
m.push(4)
m.push(5)
print(m.top())
print(m.pop())
print(m.pop())
print(m.top())
