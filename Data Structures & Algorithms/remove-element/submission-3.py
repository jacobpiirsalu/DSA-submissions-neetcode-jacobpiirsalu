class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap = 0
        search = 0
        while(search < len(nums)):
            if(nums[swap] != val):
                search=swap
                swap+=1
                search+=1
            else:
                search=swap+1
                while(search < len(nums) and nums[search] == val):
                    search+=1
                if(search < len(nums)):
                    #swap 2 values
                    nums[swap] = nums[search]
                    nums[search] = val
        return swap
                



        