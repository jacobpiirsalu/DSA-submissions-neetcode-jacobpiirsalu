import heapq
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} #nums[i] : maxheap of idx
        for i in range(len(nums)):
            if nums[i] in hmap:
                heapq.heappush(hmap[nums[i]],-i)
            else:
                newHeap = [-i]
                heapq.heapify(newHeap)
                hmap[nums[i]] = newHeap
        
        print(hmap)
        for i in range(len(nums)):
            if target-nums[i] in hmap:
                secondidx = -1*heapq.heappop(hmap[target-nums[i]])
                if secondidx == i and len(hmap[target-nums[i]]) == 0:
                    continue
                if secondidx == i:
                    secondidx = -1*heapq.heappop(hmap[target-nums[i]])
                return [i, secondidx]


        