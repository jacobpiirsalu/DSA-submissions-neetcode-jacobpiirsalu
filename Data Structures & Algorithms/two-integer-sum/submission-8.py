class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,val in enumerate(nums):
            hashmap[val] = i
        
        print(hashmap)
        for i,val in enumerate(nums):
            print(f'{val} : {i}')
            if target-val in hashmap and i!=hashmap[target-val]:
                return [i, hashmap[target-val]]
        


        