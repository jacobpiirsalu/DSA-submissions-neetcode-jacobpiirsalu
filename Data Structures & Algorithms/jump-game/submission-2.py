class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def jump(i):
            if i>=len(nums)-1:
                memo[i] = True
                return True
            if nums[i] == 0 and i<len(nums)-1:
                memo[i] = False
                return False
            
            if i in memo:
                return memo[i]
            else:
                for j in range(1, nums[i]+1):
                    memo[j+i] = jump(j+i)
                    if memo[j+i]:
                        return True
                return False

        
        return jump(0)
