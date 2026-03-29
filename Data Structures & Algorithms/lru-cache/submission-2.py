class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.lruQ = deque()

        

    def get(self, key: int) -> int:
        if key in self.keys:
            if key in self.lruQ: self.lruQ.remove(key) #O(n)
            self.lruQ.append(key)
            return self.keys[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys.update({key: value})
            self.lruQ.remove(key)
            self.lruQ.append(key)
        else: #new key
            if len(self.keys) < self.capacity:
                self.keys.update({key: value})
                self.lruQ.append(key)
            else:
                keyToRemove = self.lruQ.popleft()
                self.keys.pop(keyToRemove)
                self.keys.update({key: value})
                self.lruQ.append(key)






           


        
