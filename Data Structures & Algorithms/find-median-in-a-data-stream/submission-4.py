import heapq
class MedianFinder:

    def __init__(self):
        self.LMaxHeap = []
        self.RMinHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.LMaxHeap, -num)
        val = heapq.heappop(self.LMaxHeap)
        heapq.heappush(self.RMinHeap, -val)

        if len(self.LMaxHeap) < len(self.RMinHeap):
            val = heapq.heappop(self.RMinHeap)
            heapq.heappush(self.LMaxHeap, -val)
            return
        
        

    def findMedian(self) -> float:
        if len(self.LMaxHeap) > len(self.RMinHeap):
            print(self.LMaxHeap)
            print(self.RMinHeap)
            return -self.LMaxHeap[0]
        elif len(self.LMaxHeap) == len(self.RMinHeap):
            return (-self.LMaxHeap[0] + self.RMinHeap[0])/2
        else: print('this should not happen')
        
        