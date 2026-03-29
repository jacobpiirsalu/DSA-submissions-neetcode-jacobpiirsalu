from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        dq = intervals
        l=0
        while l<len(dq)-1:
            if dq[l+1][0] <=dq[l][1]:
                
                end = dq[l+1][1] if dq[l+1][1] > dq[l][1] else dq[l][1]
                newInterval = [dq[l][0],end]
                dq.pop(l)
                dq[l] = newInterval
                print(f'{dq}, l:{l}')
                continue
            else:
                l+=1
        
        return list(dq)