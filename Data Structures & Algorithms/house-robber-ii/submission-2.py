# we can either rob the first house and not the last, or the last house and not the first
# eg: 2 9 8 3 6
# rob: [2 9 8 3] or [9 8 3 6]
# other than that, the DP algo is the same, we either do: money[i] + rob(arr[i+2:]), skipping the adjacent house
# OR: rob(arr[i+1:]), skipping the current house

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def robN(houses):
            dp = [0,0]
            for i in range(len(houses)):
                tmp = dp[1]
                dp[1] = max(houses[i]+dp[0], dp[1])
                dp[0] = tmp
            return dp[1]


        return max(robN(nums[:-1]),robN(nums[1:]))
        