class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        sumlst = []
        curSum = []
        def dfs(i):
            
            if sum(curSum) > target:
                return
            if sum(curSum) == target:
                sumlst.append(curSum.copy())
                return
            if i>=len(nums):
                return
            
            # append and stay at this value
            curSum.append(nums[i])
            dfs(i)

            #backtrack and go to the nextvalue
            curSum.pop()
            dfs(i+1)



        
        dfs(0)
        return sumlst


        