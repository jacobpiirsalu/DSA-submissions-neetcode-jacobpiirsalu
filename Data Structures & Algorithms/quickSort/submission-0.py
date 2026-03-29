from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def realQuickSort(self, arr: List[Pair], startIdx: int, endIdx: int):
        # base case
        if endIdx-startIdx <= 0:
            return arr
        
        pivot = arr[endIdx]
        swap_ptr = startIdx
        list_ptr = startIdx
        
        while list_ptr < endIdx:
            if arr[list_ptr].key < pivot.key:
                # actually swap the value if it's strictly less than
                tmp_val = arr[list_ptr]
                arr[list_ptr] = arr[swap_ptr]
                arr[swap_ptr] = tmp_val
                swap_ptr+=1

            
            list_ptr+=1
            
        # swap the pivot
        tmp_val = arr[swap_ptr]
        arr[swap_ptr] = pivot
        arr[endIdx] = tmp_val
        
        self.realQuickSort(arr, startIdx, swap_ptr-1)
        self.realQuickSort(arr, swap_ptr+1, endIdx)
        return arr
        
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.realQuickSort(pairs, 0, len(pairs)-1)