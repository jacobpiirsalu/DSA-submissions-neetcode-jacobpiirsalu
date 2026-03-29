class Solution:
    def path(self, nums: List[int], currSubset: List[int], subsets: List[List[int]]):
        if not nums:
            subsets.append(currSubset)
            return 
        self.path(nums[1:], currSubset.copy(), subsets) #do not include
        #must copy currSubset so the original underlying object is NOT mutated
        #in further recursive calls

        #include that num in the subset
        currSubset.append(nums[0])
        self.path(nums[1:], currSubset.copy(), subsets)
        return
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.path(nums, [], subsets)
        return subsets
        

    

        
        