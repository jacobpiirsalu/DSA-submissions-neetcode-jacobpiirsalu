class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = [float('inf')]
        

    def push(self, val: int) -> None:
        if val <= self.minVals[-1]:
            self.minVals.append(val)

        self.stack.append(val)
        

    def pop(self) -> None:
        if self.top() == self.minVals[-1]:
            self.minVals.pop()

        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVals[-1]
        
