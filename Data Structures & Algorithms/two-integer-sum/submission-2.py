class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = set(nums)
        for idx,val in enumerate(nums):
            if target-val in numset:
                print(target-val)
                try:
                    secondValIdx = nums.index(target-val, idx+1)
                    return [idx, secondValIdx]
                except ValueError:
                    continue

                
        