class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for k,v in freqMap.items():
            if v == 1:
                return k
        