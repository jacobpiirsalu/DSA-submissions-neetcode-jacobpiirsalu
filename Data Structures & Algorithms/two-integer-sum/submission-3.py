class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #val:idx
        for idx,num in enumerate(nums):
            if target-num in hashmap.keys():
                return sorted([idx, hashmap[target-num]])
            else:
                hashmap.update({num:idx})


                
        