from collections import deque
class TimeMap:

    def __init__(self):
        self.hmap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap: self.hmap[key] = deque([(value, timestamp)])
        else:
            self.hmap[key].appendleft((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hmap:
            for i in range(len(self.hmap[key])):
                if self.hmap[key][i][1] <= timestamp:
                    return self.hmap[key][i][0]
        
        return ""
        
        
