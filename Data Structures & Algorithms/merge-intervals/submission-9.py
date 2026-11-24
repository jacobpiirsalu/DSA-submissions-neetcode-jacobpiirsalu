class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]

        l = 0
        for i, invl in enumerate(intervals):
            print(ret[l])
            start1, end1 = ret[l][0],ret[l][1]
            start2, end2 = invl[0], invl[1]

            if start2<=end1:
                ret[l] = [start1,max(end1,end2)] #max is needed, sort on 2nd val not gauranteed
            else:
                ret.append([start2,end2])
                l+=1
        return ret