class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self):
        self.head: Node = None # this will eventually point to another node
        self.size = 0

    def get(self, index: int) -> int:
        nodeToReturn = self.head
        if self.size <= 0 or index >= self.size or index <0:
            return -1

        for i in range(index): #index ==2 -> 0,1
            nodeToReturn = nodeToReturn.nextNode

        # [5, 2, 1, 3, 4,]
        return nodeToReturn.value


    def insertHead(self, val: int) -> None:
        prevHead = self.head
        newHead = Node(val, prevHead)
        self.head = newHead
        self.size+=1

        print("size: " + str(self.size))


    def insertTail(self, val: int) -> None:
        print("insertTail()" + str(val))
        
        
        if self.size == 0:
            self.insertHead(val)
        else:
            prevTail = self.head
            for i in range(self.size-1): #index of last element index=3 for i in [0,1,2]
                prevTail = prevTail.nextNode

            prevTail.nextNode = Node(val, None)
            self.size+=1
            print("size: " + str(self.size))
        
        

    def remove(self, index: int) -> bool:
        if self.size <= 0 or index >= self.size or index<0:
            print("size: " + str(self.size))
            return False

        elif index==0: #removal of head
            newHead = self.head.nextNode
            self.head.nextNode = None
            self.head = newHead
            self.size-=1

            print("size: " + str(self.size))
            return True

        elif index == self.size-1: #removal from tail
            priorNode = self.head
            for i in range(index-1):
                priorNode = priorNode.nextNode

            priorNode.nextNode = None
            print("size: " + str(self.size))
            self.size-=1
            return True
        
        else:
            priorNode = self.head
            for i in range(index-1):
                priorNode = priorNode.nextNode

            posteriorNode = priorNode.nextNode.nextNode
            priorNode.nextNode.nextNode = None
            priorNode.nextNode = posteriorNode
            self.size-=1

            print("head value: " + str(self.head.value))
            print("size value: " + str(self.size))
            return True

        
        
    def getValues(self) -> List[int]:
        if self.size==0:
            return []
        else:
            print("hit get values")
            listToReturn = []
            currNode = self.head
            for i in range(self.size):
                listToReturn.append(currNode.value)
                currNode = currNode.nextNode
            return listToReturn

        
