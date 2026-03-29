class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lstSubsets = []

        currSubset = []
        def dfs(i):
            if i == len(nums):
                lstSubsets.append(currSubset.copy())
                return
            
            #actually adding the value to the subset
            currSubset.append(nums[i])
            dfs(i+1)
            currSubset.pop()

            # not adding the value
            dfs(i+1)



        
        dfs(0)
        return lstSubsets

        