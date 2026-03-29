class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-1001, 0]
        for i in range(len(nums)):
            dp[1] += nums[i]
            dp[0]=max(dp[0], dp[1])
            if dp[1]<0: dp[1]=0
            
        return dp[0]
