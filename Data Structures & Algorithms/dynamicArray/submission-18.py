class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.tail = 0
        self.array = [None] * self.size
        


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        
        if self.tail <= self.size - 1:
            self.array[self.tail] = n
        else:
            # resize array
            self.resize()
            self.array[self.tail] = n

        self.tail+=1
            
        
        
            

    def popback(self) -> int:
        
        returnVal = self.array[self.tail-1]
        self.array[self.tail-1] = None
        self.tail-=1

        return returnVal
 

    def resize(self) -> None:
        # resize array
        tempArr = []
        for i in range(0, self.size):
            tempArr.append(self.array[i])

        for i in range(self.size, self.size*2):
            tempArr.append(None)

        self.size = self.size*2
        self.array = tempArr


    def getSize(self) -> int:
        return self.tail
        
    
    def getCapacity(self) -> int:
        return self.size
