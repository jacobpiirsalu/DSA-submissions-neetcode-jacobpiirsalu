class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        b = [0]*3
        for i in range(len(nums)):
            b[nums[i]] +=1

        print(b)
        k = 0
        for i in range(len(b)):
            for j in range(b[i]):
                nums[k] = i
                k+=1
        

        