class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hset = set()
        for num in nums:
            if num in hset:
                hset.remove(num)
            elif num not in hset:
                hset.add(num)
        return list(hset)[0]
        