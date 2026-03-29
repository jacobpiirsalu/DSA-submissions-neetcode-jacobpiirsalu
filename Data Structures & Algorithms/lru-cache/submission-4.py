from collections import OrderedDict
class LRUCache:
    #push new keys to end
    #pop from front

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderedHmap = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.orderedHmap:
            self.orderedHmap.move_to_end(key)
            return self.orderedHmap[key]
        return -1

        

    def put(self, key: int, value: int) -> None:
        self.orderedHmap[key] = value
        self.orderedHmap.move_to_end(key)
       
        if len(self.orderedHmap) > self.capacity:
            #no room, we need to boot out the LRU key
            self.orderedHmap.popitem(last=False) #pops item on left
            
        

        

        
