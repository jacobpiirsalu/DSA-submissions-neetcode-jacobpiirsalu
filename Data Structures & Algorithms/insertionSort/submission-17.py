# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs: return pairs
        steps = [pairs.copy()]

        for i in range(1, len(pairs)):
            swap = i
            while swap>0 and pairs[swap].key < pairs[swap-1].key:
                tmp =pairs[swap-1]
                pairs[swap-1] = pairs[swap]
                pairs[swap] = tmp
                swap-=1
                
            steps.append(pairs.copy())
                
        return steps
            

        