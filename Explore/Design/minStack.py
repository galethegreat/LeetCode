class NoMinStackError(Exception):
    pass

from collections import deque
class MinStack:

    def __init__(self):
        self._stack = deque()
        
    def push(self, val: int) -> None:
        assert -2**31 <= val <= 2**31 - 1, f"{val} must be between -2^31 <= val <= 2^31 - 1"

        if self._stack:

            cur_min = min(val, self._stack[-1][1])
            self._stack.append((val, cur_min))

        else:
            self._stack.append((val, val))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        if not self._stack:
            raise NoMinStackError('No min value in stack, stack empty')

        return self._stack[-1][1]
