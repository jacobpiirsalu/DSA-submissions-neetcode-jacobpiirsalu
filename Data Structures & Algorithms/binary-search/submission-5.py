class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binsearch(L,R):
            if L>R:
                return -1
            M=(L+R)//2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                return binsearch(M+1, R)
            else:
                return binsearch(L, M-1)
        
        return binsearch(0, len(nums)-1)