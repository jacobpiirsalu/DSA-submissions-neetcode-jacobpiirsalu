class TimeMap:

    def __init__(self):
        self.hmap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = [(value, timestamp)]
        else:
            self.hmap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        else:
            arr = self.hmap[key]
            l,r = 0, len(arr)-1
            res=""
            while l<=r:
                m = (l+r)//2
                prev_timestamp = arr[m][1]
                
                if prev_timestamp <= timestamp:
                    res = arr[m][0]
                    l=m+1
                else:
                    r=m-1
            return res

        
