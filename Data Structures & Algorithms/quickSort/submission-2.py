# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def recurseQSort(self, s:int, e:int, lst: List[Pair]):
        if e-s <=0:
            return
        
        pivot = lst[e]
        k = s
        for i in range(s, e+1):
            if lst[i].key < pivot.key:
                tmp = lst[i]
                lst[i] = lst[k]
                lst[k] = tmp
                k+=1
        #swap the pivot in
        tmp = lst[k]
        lst[k] = lst[e]
        lst[e] = tmp
        self.recurseQSort(s, k-1, lst)
        self.recurseQSort(k+1, e, lst)

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.recurseQSort(0, len(pairs)-1, pairs)
        return pairs
        