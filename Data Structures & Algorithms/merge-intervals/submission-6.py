class Solution:
    def isOverlap(self, a, b) -> (bool, List[int]):
        start1, end1 = a
        start2, end2 = b
        if start2 <= end1:
            return True, [start1, max(end1, end2)]
        else:
            return False, []
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        #print(intervals)
        ret = [intervals[0]]

        for i in range(1, len(intervals)):
            a,b = self.isOverlap(ret[-1], intervals[i])
            print(i)
            if a:
                ret[-1] = b
            else:
                ret.append(intervals[i])
        return ret