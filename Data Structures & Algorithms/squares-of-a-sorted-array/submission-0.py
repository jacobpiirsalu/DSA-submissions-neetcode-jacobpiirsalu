# trivial solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            ret.append(num**2)
        ret.sort()

        return ret