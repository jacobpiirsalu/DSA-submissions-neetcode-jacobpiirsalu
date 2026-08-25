class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        
        while L <= R:
            M = (L+R)//2
            if nums[M] == target:
                return M
            elif nums[M] > target:
                #search left
                R = M-1
                continue
            elif nums[M] < target:
                #search right
                L = M+1
                continue
            

        return -1