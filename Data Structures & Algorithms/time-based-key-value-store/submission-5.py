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
            s,e = 0, len(self.hmap[key])-1
            while s<=e:
                print(f's:{s} e:{e}')
                m = (s+e)//2
                if self.hmap[key][m][1] <= timestamp:
                    if m>0 and self.hmap[key][m-1][1] > timestamp:
                        return self.hmap[key][m][0]
                    elif m==0:
                        return self.hmap[key][m][0]
                    else: #search left half
                        e=m-1
                else: # too far in the right half, move left
                    s=m+1


            # for i in range(len(self.hmap[key])): #could be made more efficient with binary search
            #     if self.hmap[key][i][1] <= timestamp:
            #         return self.hmap[key][i][0]
        
        return ""
        
        
