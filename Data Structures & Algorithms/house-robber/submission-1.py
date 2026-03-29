class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robN(numHouses, visited, cache) -> int:
            # print(cache)
            if len(nums)%2 == 0 and numHouses>len(nums)//2:
                # print('I returned')
                return cache.get(numHouses-1, cache[numHouses-2])
            if len(nums)%2 != 0 and numHouses>len(nums)//2+1:
                # print('I returned')
                return cache.get(numHouses-1, cache[numHouses-2])
            
            validIdx = list(range(0, len(nums)))
            for idx in visited:
                # FIX 1: Safely remove neighbors (try/except block caused skipping)
                if idx-1 in validIdx: validIdx.remove(idx-1)
                if idx in validIdx: validIdx.remove(idx)
                if idx+1 in validIdx: validIdx.remove(idx+1)
            # print(validIdx)
            

            # get the 2nd max from the valid idxs
            arr = []
            vals = {}
            maxVal = 0
            for i in validIdx:
                arr.append(nums[i])
                vals[nums[i]] = i
            
            if len(arr) >0: maxVal = max(arr)

            
            if numHouses not in cache:
                # print(f'= {maxVal} + {cache[numHouses-1]}') 
                cache[numHouses] = maxVal + cache[numHouses-1]

            newVisited = visited + [vals[maxVal]] if maxVal!=0 else visited.copy()
            # print(newVisited)
            
            # FIX 2: Pass 'newVisited' directly (it already contains 'visited')
            return robN(numHouses+1, newVisited, cache)

        #max even, max odd
        if not nums: return 0
        if 0 < len(nums) <2: return max(nums)
        even = nums[::2]
        evenidx = even.index(max(even))*2
        #print(max(even))
        
        odd = nums[1::2]
        oddidx = odd.index(max(odd))*2 + 1 if odd else 0
        #print(max(odd))

        # FIX 3: Start at robN(2, ...) because cache already has data for 1 house
        return max(robN(2, [evenidx], cache = {0:0, 1 : max(even)}), robN(2, [oddidx], cache = {0:0, 1 : max(odd)}))