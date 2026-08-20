class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #timsort/quicksort (O(nlogn))
        l, r = 0,1
        while r < len(nums):
            if nums[l] != nums[r]:
                l+=1
                r+=1
            elif nums[l] == nums[r]:
                return True
        return False
        #overall time complexity: O(n + nlogn) = O(nlogn)
