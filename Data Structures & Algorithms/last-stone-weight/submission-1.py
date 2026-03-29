class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x = abs(heapq.heappop(heap))
            y = abs(heapq.heappop(heap))
            if x == y:
                continue
            if x < y:
                heapq.heappush(heap, -1*(y-x))
            else:
                heapq.heappush(heap, -1*(x-y))
        return abs(heap[0]) if heap else 0