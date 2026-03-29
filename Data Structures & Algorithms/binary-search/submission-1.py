class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        m=(l+r)//2

        while l<=r:
            if target < nums[m]:
                r=m-1
            elif target > nums[m]:
                l=m+1
            else:
                return m
            m=(l+r)//2

        return -1