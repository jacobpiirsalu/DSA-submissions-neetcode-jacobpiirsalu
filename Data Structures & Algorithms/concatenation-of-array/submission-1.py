class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #ans = 2*nums
        ans = [0] * (2*len(nums))
        for i in range(len(nums)):
            ans[i] = nums[i]
        for j in range(len(nums), 2*len(nums)):
            ans[j] = nums[j-len(nums)]
        
        return ans
        