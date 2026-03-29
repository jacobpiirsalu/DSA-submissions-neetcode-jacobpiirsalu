# you can either maintain a sorted list
# or a min-heap which is holding the "top k" largest elements, 
# since the smallest of the top k largest would be at the top of the min-heap, when we add a new value we just push to it and then pop the smallest when our size is larger than k
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
