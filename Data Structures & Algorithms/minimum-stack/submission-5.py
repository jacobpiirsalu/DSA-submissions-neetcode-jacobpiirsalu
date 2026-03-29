class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = [2**31]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if val <= self.minstk[-1]:
            self.minstk.append(val)
        

    def pop(self) -> None:
        x = self.stk.pop()
        if x == self.minstk[-1]:
            self.minstk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]
        
