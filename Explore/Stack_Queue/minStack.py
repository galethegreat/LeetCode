class MinStack(object):
    def __init__(self):
        self.stack = list()

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)


minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.top();    #// return 0
minStack.getMin(); #// return -2
