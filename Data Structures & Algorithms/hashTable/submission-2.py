class HashTable:
    
    def __init__(self, capacity: int=2):
        self.capacity = capacity
        self.hashtable = [None] * self.capacity
        self.size = 0


    def insert(self, key: int, value: int) -> None:
        idx = key % self.capacity
        if self.hashtable[idx] is None or self.hashtable[idx][0] == key:
            self.hashtable[idx] = (key,value)
        else:
            for i in range(self.capacity):
                newIdx = (idx + i) % self.capacity
                if self.hashtable[newIdx] is None:
                    self.hashtable[newIdx] = (key,value)
                    break
        
        self.size+=1
        if self.size*2 >=self.capacity:
            self.resize()


    def get(self, key: int) -> int:
        idx = key % self.capacity
        if self.hashtable[idx] is None:
            return -1
        # if self.hashtable[idx][0] == key:
        #     return self.hashtable[idx][1]
        else:
            for i in range(self.capacity):
                newIdx = (idx+i)%self.capacity
                if self.hashtable[newIdx] is not None and self.hashtable[newIdx][0] == key:
                    return self.hashtable[newIdx][1]     
        return -1


    def remove(self, key: int) -> bool:
        idx = key % self.capacity
        if self.hashtable[idx] is None:
            return False
        # if self.hashtable[idx][0] == key:
        #     self.hashtable[idx] = None
        #     self.size-=1
        #     return True
        else:
            for i in range(self.capacity):
                newIdx = (idx+i)%self.capacity
                if self.hashtable[newIdx] is not None and self.hashtable[newIdx][0] == key:
                    self.hashtable[newIdx] = None
                    self.size-=1
                    return True
                    
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        oldTable = self.hashtable.copy()
        self.capacity*=2
        self.size=0
        self.hashtable = [None] * self.capacity
        

        for kv_pair in oldTable:
            if kv_pair is not None:
                self.insert(kv_pair[0], kv_pair[1])

