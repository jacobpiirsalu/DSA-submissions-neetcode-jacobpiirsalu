"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        q = deque() #left is front, right is the back
        q2 = deque()
        visited = {} #{node.val : node}

        startNode = Node(node.val, []) #no neighbors yet
        visited[startNode.val] = startNode
        q.append(node)
        q2.append(startNode)

        while q:
            #BFS on OG graph
            lenQ = len(q)
            for i in range(lenQ):
                graphNode = q.popleft()
                curr = q2.popleft()
                for n in graphNode.neighbors:
                    if n.val in visited:
                        curr.neighbors.append(visited[n.val])
                    else:
                        newNode = Node(n.val, [])
                        curr.neighbors.append(newNode)
                        visited[newNode.val] = newNode
                        q2.append(newNode)
                        q.append(n)

                    
                    


        return startNode


