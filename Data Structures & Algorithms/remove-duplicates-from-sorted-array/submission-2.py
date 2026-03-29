class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_ptr = 1
        r_ptr = 1

        while(r_ptr < len(nums)):
            if(nums[r_ptr] != nums[r_ptr-1]):
                #new val found, write to L-ptr spot
                nums[l_ptr] = nums[r_ptr]
                l_ptr+=1
            
            r_ptr+=1
        
        return l_ptr
