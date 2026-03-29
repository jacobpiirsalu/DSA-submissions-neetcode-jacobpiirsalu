class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr = 0
        r_ptr = len(nums)-1

        while l_ptr <= r_ptr:
            mid = (r_ptr - l_ptr)//2 + l_ptr #prevent out of bounds
            if nums[mid] < target: #guess is too small
                l_ptr = mid+1
            elif nums[mid] > target:
                r_ptr = mid-1
            else:
                return mid
        
        return -1
        