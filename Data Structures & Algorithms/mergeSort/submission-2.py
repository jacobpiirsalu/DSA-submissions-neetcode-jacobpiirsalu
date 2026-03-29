class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def merge(self, arr: List[Pair], startIdx: int, midIdx: int, endIdx: int):
        l_arr_ptr = startIdx
        r_arr_ptr = midIdx+1
        
        arr_to_merge = []
        while l_arr_ptr < midIdx+1 or r_arr_ptr < endIdx+1:
            if l_arr_ptr < midIdx+1 and r_arr_ptr < endIdx+1: #both ptrs in bounds
                if arr[l_arr_ptr].key <= arr[r_arr_ptr].key:
                    arr_to_merge.append(arr[l_arr_ptr])
                    l_arr_ptr+=1
                    
                else:
                    arr_to_merge.append(arr[r_arr_ptr])
                    r_arr_ptr+=1
            else:
                if r_arr_ptr >= endIdx+1: #right ptr out of bounds
                    # add from left
                    arr_to_merge.append(arr[l_arr_ptr])
                    l_arr_ptr+=1
                else: #left is out of bounds
                    arr_to_merge.append(arr[r_arr_ptr])
                    r_arr_ptr+=1
                    
        # overwrite that section with the new array
        
        i = startIdx
        for e in arr_to_merge:
            arr[i] = e
            i+=1
                
        
    def realMergeSort(self, arr: List[Pair], startIdx: int, endIdx: int):
        if endIdx-startIdx+1 <=1: #base case, array with 1 element
           return arr
       
        midIdx = (startIdx + endIdx) // 2
           
        self.realMergeSort(arr, startIdx, midIdx)
        self.realMergeSort(arr, midIdx+1, endIdx)
       
        self.merge(arr, startIdx, midIdx, endIdx)
        return arr
         
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.realMergeSort(pairs, 0, len(pairs)-1)