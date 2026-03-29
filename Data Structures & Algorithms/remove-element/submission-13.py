class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[swap] = nums[i]
                swap+=1
        return swap