class MinStack:

    def __init__(self):
        self.stack = []
        self.minValStack = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minValStack[-1]:
            self.minValStack.append(val)

    def pop(self) -> None:
        popVal = self.stack.pop()
        if popVal <= self.minValStack[-1]:
            self.minValStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # return min(self.stack) cheating
        return self.minValStack[-1]

        
