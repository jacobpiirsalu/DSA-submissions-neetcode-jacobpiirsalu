class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        hashset = set()

        revSum = 0
        for i in range(len(nums)-1, -1, -1):
            revSum+=nums[i]
            hashset.add((revSum, i))
        
        summ=0
        for i,n in enumerate(nums):
            summ+=n
            if (summ,i) in hashset:
                return i
        return -1