class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums) % 2 ==0:
            return (self.nums[(len(self.nums)-1)//2] + self.nums[(len(self.nums)-1)//2 + 1])/2
        return self.nums[(len(self.nums)-1)//2]
        
        