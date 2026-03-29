class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tally = [0]*3  #3 possible values
        for i in range(len(nums)):
            tally[nums[i]]+=1
        
        ctr = 0
        for i in range(len(tally)):
            for j in range(tally[i]):
                nums[ctr] = i
                ctr+=1

        

        
        