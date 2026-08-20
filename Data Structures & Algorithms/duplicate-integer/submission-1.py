class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # optimal solution: hash set
        hset = set()
        for p in range(len(nums)):
            if nums[p] in hset: #O(n)
                return True
            hset.add(nums[p])
        return False
