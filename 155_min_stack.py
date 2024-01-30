import sys

class MinStack:

    def __init__(self):
        self._stack = []
        self._min = sys.maxsize 

    def push(self, val: int) -> None:
        if val < self._min:
            self._min = val

        self._stack.append(val)
        

    def pop(self) -> None:
        t = self._stack.pop()
        if t == self._min:
            self._min = sys.maxsize
            for num in self._stack:
                if num < self._min:
                    self._min = num

    def top(self) -> int:
        return self._stack[len(self._stack)-1]

    def getMin(self) -> int:
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()