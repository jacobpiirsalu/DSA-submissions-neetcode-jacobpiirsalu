class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        print(intervals)
        for i in range(len(intervals)):
            currInt = intervals[i]
            #print(currInt)
            if currInt[0] <= ret[-1][1]:
                ret[-1][1] = max(currInt[1], ret[-1][1])
            else:
                ret.append(currInt)
        return ret

