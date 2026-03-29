class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        swap = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            #swap
            nums[swap] = nums[i]
            swap+=1
        return swap

        