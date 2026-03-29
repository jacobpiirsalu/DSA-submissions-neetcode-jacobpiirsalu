class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                pivot = i+1

        def binSearch(lst,s,e):
            while s<=e:
                m=(s+e)//2
                if lst[m] == target:
                    return m
                elif lst[m]<target:
                    s=m+1
                else:
                    e=m-1
            return -1
        
        idx1 = binSearch(nums, pivot, len(nums)-1)
        idx2 = binSearch(nums, 0, pivot-1)
        if idx1 != -1 or idx2!=-1:
            return idx1 if idx1 != -1 else idx2
        return -1