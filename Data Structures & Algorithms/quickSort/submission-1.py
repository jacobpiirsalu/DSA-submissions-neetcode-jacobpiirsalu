from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def realQuickSort(self, arr: List[Pair], start_idx: int, end_idx: int):
        if end_idx-start_idx <=0:
            return arr
        
        pivot = arr[end_idx]

        swap_ptr = start_idx
        list_ptr = start_idx

        while list_ptr < len(arr):
            if arr[list_ptr].key < pivot.key:
                tmp = arr[swap_ptr]
                arr[swap_ptr] = arr[list_ptr]
                arr[list_ptr] = tmp
                swap_ptr+=1
            list_ptr+=1

        #swap pivot to swap_ptr
        tmp = arr[swap_ptr]
        arr[swap_ptr] = pivot
        arr[end_idx] = tmp

        self.realQuickSort(arr, start_idx, swap_ptr-1)
        self.realQuickSort(arr, swap_ptr+1, end_idx)
        return arr

        
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.realQuickSort(pairs, 0, len(pairs)-1)