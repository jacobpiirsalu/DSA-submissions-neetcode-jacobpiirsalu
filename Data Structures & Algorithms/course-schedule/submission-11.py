class Node:
    def __init__(self, val: int, nxt: Node):
        self.val = val
        self.nxt = nxt


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not prerequisites[0]:
            return True
       
        adjLst = {} #node.val : [neighbors]

        # build adjacency list
        for n in prerequisites:
            nodeVal = n[1]
            neighbor = n[0]
            if nodeVal in adjLst: adjLst[nodeVal].append(neighbor)
            else: adjLst[nodeVal] = [neighbor]

            if neighbor not in adjLst: adjLst[neighbor] = []

        q = deque() #left is front, right is back
        visited = set()

        # find the starting node
        # this node is not a neighbor to any other node (only outgoing connections)
        for nodeVal,nei in adjLst.items():
            ctr = 0
            for _, lst in adjLst.items():
                if nodeVal in lst:
                    ctr+=1
            if ctr == 0:
                q.append(nodeVal)
                       
        if not q: return False #no valid start node
        
        courseCtr = 0
        while q:
            #print(courseCtr)
            lenQ = len(q)
            for i in range(lenQ):
                curr = q.popleft()
                for nei in adjLst[curr]: #neighbors of curr
                    if [nei, curr] not in prerequisites: #we've already seen this edge or it's invalid
                        return False
                        
                    q.append(nei)
                    prerequisites.remove([nei,curr])
                    # as we travel along each edge of the graph described in
                    # prerequisites, we cross it off the list bc we can't
                    # travel along the same edge again, or we have a cycle
                    
                    
        return len(prerequisites) == 0 #we've travelled along every possible edge once



        
        


            


        

        