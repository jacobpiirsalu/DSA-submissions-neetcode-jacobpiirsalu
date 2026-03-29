import math
class Solution:
    def hrsOfConsumption(self, piles: List[int], kt: int):
        s = 0
        for i in range(len(piles)):
            s+= math.ceil(piles[i]/kt)
        return s
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        e = max(piles)
        s = 1
        while e>=s:
            m = (e+s)//2
            print(f"s: {s}, e: {e}, m: {m}")
            if m<=1:
                return 1

            ht = self.hrsOfConsumption(piles, m)

            if ht <= h:
                a = self.hrsOfConsumption(piles, m-1)
                if a > h:
                    return m
                e = m-1
            else:
                s = m+1
        

        return -1

        