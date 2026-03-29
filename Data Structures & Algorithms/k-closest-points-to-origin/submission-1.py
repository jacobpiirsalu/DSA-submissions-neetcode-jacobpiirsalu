import heapq
class Point:
    def __init__(self, point: List[int]):
        self.distance = -1*(point[0]**2 + point[1]**2)**0.5 #we want a max queue
        self.point = point
    def __lt__(self, other):
        return self.distance < other.distance
class Solution:
    #brute force, generate a list the distances, sort by distance, map each distance to the point
    # priority queue/heap seems like it could be useful here
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = [Point(point) for point in points]
        heapq.heapify(pts)

        while len(pts) > k:
            heapq.heappop(pts)
        
        return [point.point for point in pts]


        