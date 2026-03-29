# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs: List[Pair], s: int, m: int, e: int):
        a = 0
        al = pairs[s:m+1]
        b = 0
        bl = pairs[m+1:e+1]
        i = s

        while a<len(al) and b<len(bl):
            if al[a].key <= bl[b].key:
                pairs[i] = al[a]
                i, a = i+1, a+1
            else:
                pairs[i] = bl[b]
                i, b = i+1, b+1
            
        while a<len(al):
            pairs[i] = al[a]
            i, a = i+1, a+1
        while b<len(bl):
            pairs[i] = bl[b]
            i,b = i+1, b+1


    def recurseMSort(self, pairs: List[Pair], s: int, e: int):
        #base case
        if e-s <= 0:
            return
        
        #general
        m = (s+e)//2
        self.recurseMSort(pairs, s, m)
        self.recurseMSort(pairs, m+1, e)

        self.merge(pairs, s, m, e)
        return


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.recurseMSort(pairs, 0, len(pairs)-1)
        return pairs

