class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        count=0
        maxCount=0
        for val in hset:
            if val-1 in hset:
                continue
            else:
                count+=1
                i=val+1
                while i in hset:
                    count+=1
                    i+=1
                if count>maxCount:
                    maxCount=count
                count=0
        return maxCount
                
