class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0,0]
        for i in range(len(nums)):
            nextVal = max(nums[i]+cache[0],cache[1])
            cache[0] = cache[1]
            cache[1] = nextVal
        return cache[1]