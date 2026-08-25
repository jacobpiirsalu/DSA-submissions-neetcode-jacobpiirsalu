class Solution:
    
    
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        

        def binsearch(L, R):
            M = (L+R)//2
            if L>R:
                return -1
            if nums[M] == target:
                return M
            if nums[M]<target:
                return binsearch(M+1,R)
            if nums[M]>target:
                return binsearch(L, M-1)

        return binsearch(L,R)