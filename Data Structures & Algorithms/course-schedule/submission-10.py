class Node:
    def __init__(self, val: int, nxt: Node):
        self.val = val
        self.nxt = nxt


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not prerequisites[0]:
            return True
       
        adjLst = {} #node.val : [neighbors]
        

        # startNodeIdx = None
        # for i in range(len(prerequisites)):
        #     val = prerequisites[i][1]
        #     count = 0
        #     for j in range(len(prerequisites)):
        #         if val == prerequisites[j][0]: count+=1
            
        #     if count == 0:
        #         startNodeIdx = i
        #         break

        # print(startNodeIdx)
        # if len(prerequisites) > 1 and startNodeIdx is None: return False

        for n in prerequisites:
            nodeVal = n[1]
            neighbor = n[0]
            if nodeVal in adjLst: adjLst[nodeVal].append(neighbor)
            else: adjLst[nodeVal] = [neighbor]

            if neighbor not in adjLst: adjLst[neighbor] = []

        #adjLst is built and we know where to start, now BFS
        q = deque() #left is front, right is back
        visited = set()

        # startNodeVal = prerequisites[startNodeIdx][1]
        # q.append(startNodeVal)
        # Start from the bottom, start nodes will be those with no neighbors

        courseCtr = 0
        for nodeVal,nei in adjLst.items():
            ctr = 0
            for _, lst in adjLst.items():
                if nodeVal in lst:
                    ctr+=1
            if ctr == 0:
                q.append(nodeVal)
                
                
        print(adjLst)
        if not q: return False
        
        while q:
            #print(courseCtr)
            lenQ = len(q)
            for i in range(lenQ):
                curr = q.popleft()
                
                for nei in adjLst[curr]: #neighbors of curr
                    if [nei, curr] not in prerequisites:
                        return False
                        
                    q.append(nei)
                    prerequisites.remove([nei,curr])
                    print(prerequisites)
                    courseCtr+=1
                    
                    
        return len(prerequisites) == 0



        
        


            


        

        