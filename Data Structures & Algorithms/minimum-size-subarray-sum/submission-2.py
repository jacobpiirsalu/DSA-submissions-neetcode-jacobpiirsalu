class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums)+1
        summ = 0
        l=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                minLength = min(minLength, r-l+1)
                if minLength == 2: print(f'l:{l} r:{r}')
                summ-=nums[l]
                l+=1
        print(l)
        if minLength!=len(nums)+1: return minLength
        else: return 0
            
            
            