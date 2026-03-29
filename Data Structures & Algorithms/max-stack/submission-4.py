import heapq
class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxStack = []
        self.removed = set()
        self.uid = 0
        
        

    def push(self, x: int) -> None:
        self.stack.append((x,self.uid))
        heapq.heappush(self.maxStack, (-x,-self.uid))
        self.uid+=1
        
        
        

    def pop(self) -> int:
        while self.stack and -self.stack[-1][1] in self.removed:
            self.stack.pop()
        ret = self.stack.pop()
        self.removed.add(-ret[1])
        return ret[0]
        
        

    def top(self) -> int:
        while self.stack and -self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        while self.maxStack[0][1] in self.removed:
            heapq.heappop(self.maxStack)
        return -self.maxStack[0][0]
        

    def popMax(self) -> int:
        while self.maxStack[0][1] in self.removed:
            heapq.heappop(self.maxStack)
        
        ret = heapq.heappop(self.maxStack)

        self.stack.remove((-ret[0], -ret[1]))
        print(self.stack)
        print(self.maxStack)
        return -ret[0]
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
