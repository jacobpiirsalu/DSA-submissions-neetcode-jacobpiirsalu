class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap storing the freq of each number
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        


        # while count<=k
        # loop through the hashmap, when the max freq is found, 
        # add that val to the result, count++
        # when count = k, we have the top k, stop
        print(hmap)
        count=0
        res = []
        for _ in range(k):
            print('looop')
            maxx = (0,0)
            for k,v in hmap.items():
                if v>maxx[0] and k not in res:
                    maxx=(v,k) #k,v = number, freq
            print(maxx)
            res.append(maxx[1])
        return res
                



        