class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.front, self.rear, self.size = 0,0,0
        self.capacity = k
        

    def enQueue(self, value: int) -> bool:
        
        if self.isEmpty():
            self.arr[self.rear] = value
            #print(self.rear)
            self.size+=1
            return True
        elif self.isFull():
            #print(self.rear)
            return False
        else:
            self.rear = (self.rear+1)%self.capacity
            self.arr[self.rear] = value
            self.size+=1
            
            #print(self.rear)
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        elif self.size==1:
            self.arr[self.front] = 0
            self.size-=1
            return True
        else:
            self.arr[self.front] = 0
            self.front = (self.front+1)%self.capacity
            
            self.size-=1
            print(self.arr)
            print(self.Front())
            print(self.Rear())
            return True

    def Front(self) -> int:
        return self.arr[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.arr[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()