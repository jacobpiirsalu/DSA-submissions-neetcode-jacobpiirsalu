class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def isPpairsWDiffLte(m:int):
            pcnt = 0
            i=0
            while pcnt<p and i+1<len(nums):
                diff = abs(nums[i]-nums[i+1])
                if diff <=m:
                    pcnt+=1
                    i+=2
                else: i+=1
            return pcnt>=p
        
        l,r = 0, 10**9
        ret = 10**9
        while l<=r:
            m = (l+r)//2

            if isPpairsWDiffLte(m):
                ret = m
                r=m-1
            else:
                l=m+1
        return ret