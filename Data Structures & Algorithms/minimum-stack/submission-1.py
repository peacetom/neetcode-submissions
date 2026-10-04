class MinStack:

    def __init__(self):
        self.stack = []
        # record the minimum after each operation
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        # add the smallest of the val and the current min to the min stack
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]

