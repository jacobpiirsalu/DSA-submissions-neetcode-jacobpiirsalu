class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0,len(nums)-1

        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        if l-1<0 or nums[l]>nums[l-1]:
            pivot = l
        else:
            pivot = l-1

        def binsearch(nums, start, end):
            if start>end:
                return -1
            m=(start+end)//2
            print(f'start: {start} end: {end}')
            if nums[m]==target:
                return m
            elif nums[m]<target:
                return binsearch(nums, m+1,end)
            else:
                return binsearch(nums, start, m-1)
        
        #print(binsearch(nums, pivot+1, len(nums)-1))
        print(f'pivot: {pivot}')
        return max(binsearch(nums,0,pivot), binsearch(nums, pivot+1, len(nums)-1))
        