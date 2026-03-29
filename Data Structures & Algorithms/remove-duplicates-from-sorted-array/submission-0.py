class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_ptr = 0
        r_ptr = 1

        while(l_ptr != len(nums)-1):
            if(nums[l_ptr] == nums[r_ptr]):
                nums.remove(nums[l_ptr])
            else:
                l_ptr+=1
                r_ptr+=1
        
        return len(nums)