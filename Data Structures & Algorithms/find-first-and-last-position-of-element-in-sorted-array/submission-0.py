class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #edge cases:
        #1. the entire array is filled with target values
        #2. target values are at the start block or end block of the array
        s=0
        e=len(nums)-1

        ret=[-1,-1]
        while s<=e:
            m=(s+e)//2
            if nums[m] == target:
                if m==0 or (m>0 and nums[m-1] < target):
                    ret[0] = m
                    break
                else:
                    e=m-1
            elif nums[m] > target:
                e=m-1
            else:
                s=m+1

        s=0
        e=len(nums)-1
        while s<=e:
            m=(s+e)//2
            if nums[m] == target:
                if m==len(nums)-1 or (m<len(nums) and nums[m+1] > target):
                    ret[1] = m
                    break
                else:
                    s=m+1
            elif nums[m] > target:
                e=m-1
            else:
                s=m+1
        return ret



