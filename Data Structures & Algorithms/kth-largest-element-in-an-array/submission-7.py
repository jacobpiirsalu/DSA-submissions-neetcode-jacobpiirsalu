class Solution:
    def quickSelect(self, arr: List[int], startIdx: int, endIdx: int, k_largest: int) -> List[int]:
        if endIdx-startIdx <=0:
            return [arr[endIdx]]
        
        # partitioned sort
        pivot = arr[endIdx]
        
        swap_ptr = startIdx
        list_ptr = startIdx
        
        while list_ptr < endIdx:
            if arr[list_ptr] < pivot:
                # swap small value
                tmp = arr[list_ptr]
                arr[list_ptr] = arr[swap_ptr]
                arr[swap_ptr] = tmp
                
                #increment the swap ptr
                swap_ptr+=1
            list_ptr+=1
        
        # swap pivot into the swap_ptr
        tmp = arr[swap_ptr]
        arr[swap_ptr] = pivot
        arr[endIdx] = tmp
        
        # determine which half of the array to continue searching
        if len(arr) - k_largest == swap_ptr: # the pivot is at the value, we found it
            return [arr[swap_ptr]]
        else: # we need to keep searching
            if arr[len(arr) - k_largest] < arr[swap_ptr]: # search left half of array
                return self.quickSelect(arr, startIdx, swap_ptr-1, k_largest)
            else: # search right half of array
                return self.quickSelect(arr, swap_ptr+1, endIdx, k_largest)
                 
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, k)[0]