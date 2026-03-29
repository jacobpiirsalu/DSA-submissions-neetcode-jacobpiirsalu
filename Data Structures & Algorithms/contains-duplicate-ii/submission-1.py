# 2 numbers are equal within the window
# AND those two numbers are within a window of size k

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        w=k+1
        for i in range(len(nums)):
            val=nums[i]
            if i-w>=0:
                print(nums[i-w])
                window.remove(nums[i-w])
            if val in window:
                return True
            else:
                window.add(val)
        
        return False
        